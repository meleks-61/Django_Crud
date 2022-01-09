from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):#UserCreation form san inherit ediyoruz.Zaten UserCreation modeli içinde passwor1 ve password2 işlemleri mevcut biz extra User modelinden de username ve email alanlarını da alıp bu Register formuna dahil ediyoruz
    email=forms.EmailField()#email alanını zorunlu kılmak için
    class Meta:
        model=User
        fields=("username","email")
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, that one already taken ")
        return email