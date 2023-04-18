from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views
from django.conf import settings

from .forms import CustomAuthForm

urlpatterns = [

    path('detail/', views.detail, name="detail"),
    path('register/',views.register,name="register"),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name="login",kwargs={"authentication_form":CustomAuthForm}),
    path('logout/', authentication_views.LogoutView.as_view(template_name='Z_tech_website/index.html'), name="logout"),
    path('certificate/', views.Getcertificate, name='certificate'),
    path('valid', views.verification, name='valid')

]
