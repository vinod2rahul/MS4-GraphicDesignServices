from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/login/', views.handleLogin, name="login"),
    path('', views.dashboard, name="dashboard"),
    path('accounts/designs/', views.getdesigns, name="designs"),
    path('designs/<design_id>', views.getdesignsbyid, name="design"),
    path('accounts/logout/', views.handleLogout, name="logout"),
]
