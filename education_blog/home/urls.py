from django.urls import path
from .views import home,about,teacher,BranchsTeacher
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',home,name='home' ),
    path('about/',about,name='about' ),
    path('teacher/',teacher,name='teacher' ),
    path('<str:slug>/branch',BranchsTeacher,name='branchs_teacher'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login' ),#paket hazır fakat templati bizden istiyor
    path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name='logout' ),
    
]