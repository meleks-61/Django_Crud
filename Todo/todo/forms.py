from django import forms
from .models import Todo



class TodoAddForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title'] #olusturdugum form da Todo modelindeki title ı kullanmak istiyorum sadece
        
        
        
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title","completed"]
        