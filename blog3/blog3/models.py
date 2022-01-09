from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
def user_directory_path(instance,filename):
    return'blog3/{0}/{1}'.format(instance.author.id,filename)



class Category(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='cat',null=True,blank=True )
    slug=models.SlugField(blank=True, unique=True,)
   
    
    def __str__(self):
        return self.name
    







class Post(models.Model):
    
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    content=RichTextField()
    published_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=user_directory_path,null=True,blank=True )
    status=models.ForeignKey(Category,on_delete=models.CASCADE)
    #farklı kullanıcılar aynı resmi paylaştıgında adlandırma farklı olmalı ona da bir bak
    slug=models.SlugField(blank=True, unique=True)
    
   
    
    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    class Meta:
        ordering =['-published_date','id']
        
class Comment(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name='Name',default='Name')
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)
    content=RichTextField()
    approved_comment=models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment=True
        self.save()
        
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def __str__(self):
        return self.name
                             