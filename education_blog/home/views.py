from django.shortcuts import render,HttpResponse

from home.forms import ContactForm

# Create your views here.
def home(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        "form":form
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html')
def teacher(request):
    return render(request,'home/teacher.html')