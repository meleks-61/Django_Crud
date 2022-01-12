from django.shortcuts import redirect, render,HttpResponse

from home.forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()#buraya kadar gelmiş bir olay başarılıdır zaten
        messages.success(request,"Form has been sent")
        return redirect("home")
    context={
        "form":form
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html')
def teacher(request):
    return render(request,'home/teacher.html')