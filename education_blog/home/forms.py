from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Name'}),
            "number":forms.TextInput(attrs={'placeholder':'Phone'}),
            "email":forms.EmailInput(attrs={'placeholder':'Email'}),
            "message":forms.TextInput(attrs={'placeholder':'Message'})
        }#placeholderlı form alanları için