from django.urls import path
from . import views
from graphicdesignapp.views import CreateCheckOutSessionView, CreateOrderCheckOutSessionView

urlpatterns = [
    # path('', views.index, name="index"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/login/', views.handleLogin, name="login"),
    path('', views.dashboard, name="dashboard"),
    path('calculate-price/', views.calculatePrice, name="calculate"),
    path('webhook/', views.stripe_webhook, name="stripe_webhook"),
    path('success/', views.PaymentSuccess, name="success"),
    path('cancel/', views.PaymentCanceled, name="cancel"),
    path('accounts/designs/', views.getdesigns, name="designs"),
    path('designs/<design_id>', views.getdesignsbyid, name="design"),
    path('request-design/', views.requestdesign, name="requestdesign"),
    path('accounts/logout/', views.handleLogout, name="logout"),
    path('create-checkout-session/', CreateCheckOutSessionView.as_view(),
         name="create-checkout-session"),
    path('create-order-checkout-session/', CreateOrderCheckOutSessionView.as_view(),
         name="create-order-checkout-session"),
]
