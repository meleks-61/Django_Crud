from django.shortcuts import redirect, render,HttpResponse

from home.forms import ContactForm
from django.contrib import messages
from .models import Teacher

# Create your views here.
def home(request):
    teachers=Teacher.objects.all()
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()#buraya kadar gelmiş bir olay başarılıdır zaten
        messages.success(request,"Form has been sent")
        return redirect("home")
    context={
        "form":form,
        "teachers":teachers
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html')
def teacher(request):
    teachers=Teacher.objects.all()
    context={
        "teachers":teachers
    }
    return render(request,'home/teacher.html',context)