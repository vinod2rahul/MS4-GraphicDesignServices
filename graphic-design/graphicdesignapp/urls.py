from django.urls import path
from . import views
from graphicdesignapp.views import CreateCheckOutSessionView

urlpatterns = [
    # path('', views.index, name="index"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/login/', views.handleLogin, name="login"),
    path('', views.dashboard, name="dashboard"),
    path('webhook/', views.stripe_webhook, name="stripe_webhook"),
    path('success/', views.PaymentSuccess, name="success"),
    path('cancel/', views.PaymentCanceled, name="cancel"),
    path('accounts/designs/', views.getdesigns, name="designs"),
    path('designs/<design_id>', views.getdesignsbyid, name="design"),
    path('accounts/logout/', views.handleLogout, name="logout"),
    path('create-checkout-session/', CreateCheckOutSessionView.as_view(),
         name="create-checkout-session"),
]
