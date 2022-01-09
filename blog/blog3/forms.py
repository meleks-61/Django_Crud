from django import forms
from .models import Comment, Post,Category
class PostForm(forms.ModelForm):
    status=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Select Category")
    
    class Meta:
        model=Post
        fields=["title","image","content","status"]



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","content"]#kullanıcıya sunulacak kısım


#{{form.media}}