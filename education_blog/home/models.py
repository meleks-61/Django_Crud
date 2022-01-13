from types import MappingProxyType
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    number=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.name
class Branch(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='branch',null=True,blank=True)
    slug=models.SlugField(blank=True,unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
  
    
    def __str__(self):
        return self.title
    
    
    
    
    
class Teacher(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    department=models.ForeignKey(Branch,on_delete=models.CASCADE)#onetomany(foreignkey) ilişki-istediğimiz zaman branch ekleyip ordan seçim yapabilmek için brunch modeli tanımlayıp buraya relation ile bağlamlıyız.Eğer chociefield yaparsak daha sonra branch eklemek için kodu değiştirmemiz gerekebilir
    image=models.ImageField(upload_to="teacher",default="profile.jpg")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True,unique=True)
    
    def __str__(self):
        return self.name