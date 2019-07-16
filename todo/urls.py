from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landingpage/<todo_id>/<todo_text>', views.landingPage, name='landingpage'),
    path('add', views.addTodo, name='add'),
    path('edit/<todo_id>/<todo_text>', views.editTodo, name='editTodo'),
    path('save', views.saveTodo, name='save'),
    path('delete/<todo_id>', views.deleteTodo, name='deleteTodo'),
    path('deleteall', views.deleteAll, name='deleteall')
]
