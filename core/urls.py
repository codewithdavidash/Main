from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from .forms import LoginForm

urlpatterns = [
    path('', index, name='index'),
    path('admins/', admin, name='admin'),
    path('services/', services, name='services'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('aims/', aims, name='aims'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup')
]
