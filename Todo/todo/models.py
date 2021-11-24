from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True) #auto_now_add=True sadece oluşturuldugu tarihi alırken,auto_now=True güncellendiği tarihi alır. 
    
    
    class Meta:
        ordering =('-created_date',)#enson oluşturduggum title en üste koyacak(optional)->oludturulma tarihine göre tersten sırala
    def __str__(self):
        return self.title