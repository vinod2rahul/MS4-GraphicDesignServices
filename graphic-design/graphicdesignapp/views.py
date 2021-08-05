from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from graphicdesignapp.models import Design, Order
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from django.utils import timezone
import datetime
import re
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

# TODO : check this view
# def index(request):
#     return HttpResponse(content="index")


def check(email):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(email_regex, email)):
        return True
    else:
        return False


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        if len(username) >= 5 and check(email) and len(password) >= 8 and len(firstname) >= 5 and len(lastname) >= 5:
            isUserPresent = User.objects.all().filter(username=username).exists()
            # Check if email exist
            if isUserPresent:
                messages.error(request, "User with username Exist")
                return redirect('register')
            createdUser = User.objects.create(
                username=username, email=email, password=make_password(password))
            createdUser.first_name = firstname
            createdUser.last_name = lastname
            createdUser.save()
            # messages.success(request, "User Registered Successfully")
            return redirect('login')
        else:
            if len(username) < 5:
                messages.error(
                    request, "UserName should be atleast 5 characters long and not empty")
            if len(firstname) < 5:
                messages.error(
                    request, "Firstname should be atleast 5 characters long and not empty")
            if len(lastname) < 5:
                messages.error(
                    request, "Lastname should be atleast 5 characters long and not empty")
            if not check(email):
                messages.error(request, "Email must be an email")
            if len(password) < 8:
                messages.error(
                    request, "Password must be 8 characters long")
    return render(request, 'register.html')


def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) > 0 and len(password) > 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('dashboard')
            else:
                messages.error(
                    request, "Invalid Credentials, Please Try again...")
                return redirect(to='login')
        else:
            if len(username) == 0:
                messages.error(request, "Username cannot be empty")
            if len(password) == 0:
                messages.error(request, "Password Cannot Be Empty")
    return render(request, 'login.html')


def getdesigns(request):
    designs = Design.objects.all()
    serialized_data = serializers.serialize('python', designs)
    return JsonResponse(serialized_data, safe=False)


@login_required(login_url='/accounts/login')
def requestdesign(request):
    # if request.method == 'POST':
    #     size = request.POST['size']
    #     category = request.POST['cat']
    #     description = request.POST['desc']
    #     if len(size) > 0 and len(category) > 0 and len(description) > 0:
    #         createOrderView(user=request.user, category=category,
    #                         size=size, description=description)
    #     else:
    #         if len(size) == 0:
    #             messages.error(request, "Size Cannot be empty")
    #         if len(category) == 0:
    #             messages.error(
    #                 request, "Category Must be either icon, logo or poster")
    #         if len(description) == 0:
    #             messages.error(request, "Description of the order is Required")
    #         return redirect(to='requestdesign')
    return render(request, 'request_design.html')


@login_required(login_url='/accounts/login')
def getdesignsbyid(request, design_id):
    design = Design.objects.get(id=design_id)
    username = request.user
    orders = Order.objects.all().filter(user=username)
    is_paid = False
    for order in orders:
        if order.design_id == int(design_id):
            is_paid = True
            break
    return render(request, 'single_design.html', {
        'design': design,
        'is_paid': is_paid
    })


def dashboard(request):
    return render(request, 'dashboard.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout success")
    return redirect('dashboard')


def PaymentSuccess(request):
    messages.success(request, "Order SuccessFull")
    return redirect('dashboard')


def PaymentCanceled(request):
    messages.error(request, "Order Canceled")
    return redirect('dashboard')


@csrf_exempt
def calculatePrice(request):
    categories = {
        "icon": 2,
        "poster": 3,
        "logo": 5
    }
    price_of_each_px = 3
    if(request.method == "POST"):
        category = request.POST['category']
        size = int(request.POST['size'])
        totalPrice = price_of_each_px * size * categories[category]
        return JsonResponse({
            "price_per_each_px": price_of_each_px,
            "desired_size": size,
            "category_price": categories[category],
            "totalPrice": totalPrice
        })


class CreateCheckOutSessionView(View):
    def post(self, request, *args, **kwargs):
        design = Design.objects.get(id=request.POST['order_id'])
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': design.category,
                        },
                        'unit_amount': design.price,
                    },
                    'quantity': 1,
                }],
            metadata={
                "design_id": design.id,
                "username": request.user,
                "price": design.price
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(checkout_session.url, code=303)


class CreateOrderCheckOutSessionView(View):
    def post(self, request, *args, **kwargs):
        size = request.POST['size']
        category = request.POST['cat']
        description = request.POST['desc']
        price = request.POST['price']
        if len(size) > 0 and len(category) > 0 and len(description) > 0:
            YOUR_DOMAIN = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'product_data': {
                                'name': category,
                            },
                            'unit_amount': price,
                        },
                        'quantity': 1,
                    }],
                metadata={
                    "design_id": 5,
                    "username": request.user,
                    "size": size,
                    "description": description,
                    "price": price
                },
                mode='payment',
                success_url=YOUR_DOMAIN + '/success',
                cancel_url=YOUR_DOMAIN + '/cancel',
            )
            return redirect(checkout_session.url, code=303)
        else:
            if len(size) == 0:
                messages.error(request, "Size Cannot be empty")
            if len(category) == 0:
                messages.error(
                    request, "Category Must be either icon, logo or poster")
            if len(description) == 0:
                messages.error(request, "Description of the order is Required")
            return redirect(to='requestdesign')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        design_id = session["metadata"]["design_id"]
        username = session["metadata"]["username"]
        size = 0
        price = 0
        description = "This is Description"
        if session["metadata"].get("size") is not None:
            size = session["metadata"].get("size")
        if session["metadata"].get("price") is not None:
            price = int(session["metadata"].get("price"))
        if session["metadata"].get("description") is not None:
            description = session["metadata"].get("description")
        design = Design.objects.get(id=design_id)

        user = User.objects.get(username=username)
        order = Order(
            category=design.category,
            user=user,
            size=size,
            description=description,
            design_id=design.id,
            price=price,
            is_paid=True,
            paid_at=datetime.datetime.now()
        )
        order.save()
    # Passed signature verification
    return HttpResponse(status=200)
