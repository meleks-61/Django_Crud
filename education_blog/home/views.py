from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.core.paginator import Paginator
from home.forms import ContactForm,CommentForm
from django.contrib import messages
from .models import Teacher,Branch,Comment

# Create your views here.
def home(request):
    comments=Comment.objects.all()
    branchs=Branch.objects.all()
    comment=comments[0]
    items=comments[1:]
    
    form=CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home")
   
    context={
        "comment":comment,
        "items":items,
        "branchs":branchs,
        "form":form
        
        
    }
    return render(request,'home/index.html',context)

def about(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()#buraya kadar gelmiş bir olay başarılıdır zaten
        messages.success(request,"Form has been sent")
        return redirect("home")
    context={
        "form":form,
        
    }
    return render(request,'home/about.html',context)
def teacher(request):
    teacher_list=Teacher.objects.all()
    paginator=Paginator(teacher_list,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        "page_obj":page_obj
    }
   
    return render(request,'home/teacher.html',context)

def BranchsTeacher(request,slug):
    branch=get_object_or_404(Branch,slug=slug)
    teachers=Teacher.objects.filter(department=branch)
    teacher=teachers[0]
    items=teachers[1:]
    context={
        "branch":branch,
        "items":items,
        "teacher":teacher
    }
    return render(request,"home/branch_teacher.html",context)
    