from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.handleLogin, name="login"),
    path('', views.dashboard, name="dashboard"),
    path('designs/', views.getdesigns, name="designs"),
    path('logout/', views.handleLogout, name="logout"),
]
