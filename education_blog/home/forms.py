from django import forms
from .models import Contact,Comment


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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","image","content"]
        # widgets={
        #     "image":forms.ImageInput(attrs={'placeholder':'Image'}),
        #     "name":forms.TextInput(attrs={'placeholder':'Name'}),
        #     "content":forms.TextInput(attrs={'placeholder':'Content'})
        # }