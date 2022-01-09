from django.core import paginator
from django.shortcuts import render,redirect,get_object_or_404,Http404
from .models import Comment, Post,Category
from .forms import CommentForm,PostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger#peginationun görülmesi için import etttiğimiz kütüphaneler
from django.db.models import Q#aramalar için
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def index(request):
    recent_posts=Post.objects.all().order_by("-published_date")[:2]
   
    post_list=Post.objects.all()
    
    #categories
    cats=Category.objects.all()
    
    #search
    query=request.GET.get('q')
    if query:
        post_list=post_list.filter(
            Q(title__icontains=query )| Q(content__icontains=query)   #| Q(user_first_name__icontains=query)  
        ).distinct()
    
    #pegination
    paginator=Paginator(post_list,3)#bir sayfada kaçtane görülmesi gerektiğine karar veriyor
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer,deliver first page.
        posts=paginator.page(1)
    except EmptyPage:
        #if page is out of range ,deliver last page of results
        posts=paginator.page(paginator.num_pages)
           
    context={
        "posts":posts,
        "cats":cats,
        "recent_posts":recent_posts
        
    }
   
    return render(request,'index.html',context)


# def search(request):
#     posts=Post.object.all()
#     query=request.GET.get('q')
#     if query:
#         posts=posts.filter(
#             Q(title__icontains=query ) |Q(status__icontains=query) 
#         ).distinct()
#     context={
#         "posts":posts
#     }
#     return render(request,'footer.html',context)
@login_required
def post_create(request):
    
    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        return redirect("blog3:index")
    context={
        "form":form
    }
    return render(request,'post_create.html',context)

@login_required    
def post_update(request,slug):
    if  not request.user.is_authenticated():
        return Http404()
    post=get_object_or_404(Post,slug=slug)
    if request.user.id!=post.author.id:
        return redirect("index")
    form=PostForm(request.POST or None, request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect("blog3:index")
    context={
        "post":post,
        "form":form
    }
       
    return render(request,"post_create.html",context)





def post_detail(request,slug):
    
    form=CommentForm()
    obj=get_object_or_404(Post, slug=slug)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            #comment.user=request.user
            comment.post=obj
            comment.save()
            return redirect("blog3:detail",slug=slug)
    context={
        "post":obj,
        "form":form,
    }
    return render(request,'post_detail.html',context)

@login_required
def post_delete(request,slug):
    
    post=get_object_or_404(Post,slug=slug)
    if request.user.id!=post.author.id:
        return redirect("blog3:index")
    else:
        post.delete()
        return redirect("blog3:index")
        
   

@login_required
def comment_approved(request,slug):
    comment=get_object_or_404(Comment,slug=slug)
    comment.approve()
    return redirect('blog3:detail',slug=comment.post.slug)#slug=slug

@login_required
def comment_remove(request,slug):
    comment=get_object_or_404(Comment,slug=slug)
    comment.delete()
    return redirect('blog3:detail',slug=comment.post.slug)
    

    
    



def category_show(request,slug):
    
    cat=get_object_or_404(Category,slug=slug)
    items=Post.objects.filter(status=cat)
    context={
        "cat":cat,
        "items":items,
        
    }
    return render(request,'categories.html',context)
