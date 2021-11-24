from django.urls import path
from .views import home,todo_list,todo_add,todo_update,todo_delete


urlpatterns = [
    path('',home, name='home'),
    path('list/',todo_list, name='list'),#read
    path('add/',todo_add, name='add'),#create
    path('<int:id>/update',todo_update, name='update'),#create
    path('<int:id>/delete',todo_delete, name='delete'),#delete
]