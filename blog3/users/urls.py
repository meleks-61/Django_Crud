from django.urls import path
from django.contrib.auth import views as auth_views#djangonun kendi login ve logotunu kullanabilmek için
from .views import register


app_name="users"
urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logut.html"),name="logout"),
    path('register/',register,name="register")
]