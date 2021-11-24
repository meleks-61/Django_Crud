from django.shortcuts import redirect, render,get_object_or_404
from .models import Todo
from .forms import TodoAddForm,TodoUpdateForm
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request ,"todo/home.html")

def todo_list(request):
    todos=Todo.objects.all()#oluşturdugumuz Todo modelini todosa atadık
    
    ###############add formunu listeye ekledik
    
    form=TodoAddForm()#Kullanıcıdan veri alabilmek için azönce forms.py da oluşturdugumuz TodoAddFormu form a atadık template gönderebilmek için context kullandık
    if request.method=='POST':#TodoAddForm sayesinde kullanıcıdan aldıgımız veriyi burda yakaladık
        form=TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
    ##############################################
            
            
            
    context={
        "todos":todos,#trmplate modeli gönderebilmek için context oluşturmamız gerekiyor.
        "form":form
    }
    
    return render(request, 'todo/todo_list.html',context)#crud daki r(read)
def todo_add(request):
    form=TodoAddForm()#Kullanıcıdan veri alabilmek için azönce forms.py da oluşturdugumuz TodoAddFormu form a atadık template gönderebilmek için context kullandık
    if request.method=='POST':#TodoAddForm sayesinde kullanıcıdan aldıgımız veriyi burda yakaladık
        form=TodoAddForm(request.POST)
        if form.is_valid():
            form.save()#girilen bilgileri kaydettik,listeye ekledik yeni veriyi
            return redirect("list")#liste sayfasına yönlendirdik kullanıcıyı
    context={
        "form":form
    }
    return render(request, 'todo/todo_add.html',context)#crud daki c(create )için bir form oluşturmalıyız.

def todo_update(request,id):
    todo=Todo.objects.get(id=id)# get ile uniq değerler çekilir.Database deki Todo modelinde id si request içinde gelen hangi id ye eşit ise onu çek ve todo ya ata
    # todo=get_object_or_404(Todo,id=id)#datatbase deki id ile eşleşen veriyi getir yoksa 404 hatası ver
    form=TodoUpdateForm(instance=todo)#database den id si ile çağırdıgım todo yu formun içine gönderdim,kullanıcıya iletiyorum
    if request.method=="POST":
        form=TodoUpdateForm(request.POST,instance=todo)#önceden var olan ile(instance=todo,yeni girdiyi (request.POST)kıyaslayıp güncelleme yapar)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
        "form":form,
        "todo":todo,
    }
        
    return render(request,"todo/todo_update.html",context) 



def todo_delete(request,id):
    # todo=get_object_or_404(Todo,id)
    todo=Todo.objects.get(id=id)
    if request.method=="POST" :
        todo.delete()
        return redirect("list")
    context={
        "todo":todo
    }
    return render(request,'todo/todo_delete.html',context)