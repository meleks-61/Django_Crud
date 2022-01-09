from django.urls import path
from .views import index,post_detail,category_show,post_create,post_update,post_delete
app_name="blog3"
urlpatterns = [
    path('',index,name='index' ),
    path('create/',post_create,name='create' ),
    path('<str:slug>/update',post_update,name='update' ),
    path('<str:slug>/delete',post_delete,name='delete' ),
    
    path('<str:slug>',post_detail,name='detail' ),
    path('<str:slug>/category',category_show,name='category' ),
 
]