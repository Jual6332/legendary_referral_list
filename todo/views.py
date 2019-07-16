from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

numLandingPageVisits = 0;

def index(request):
    # Serve landing_page.html
    todo_list = Todo.objects.order_by('-hits')
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

def landingPage(request, todo_id, todo_text):
    # Declare global variable
    global numLandingPageVisits;
    numLandingPageVisits += 1

    # Add 1 click
    todo = Todo.objects.get(pk=todo_id)
    todo.hits += 1
    todo.save()

    # Serve landing_page.html
    todo_list = Todo.objects.order_by('-hits')
    form = TodoForm()
    context = {'todo': todo,'todo_list' : todo_list, 'form' : form, 'numLandingPageVisits': numLandingPageVisits}

    return render(request,'todo/landing_page.html',context)

@require_POST
def addTodo(request):
    # POST request
    form = TodoForm(request.POST)

    # Save new item
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def editTodo(request,todo_id,todo_text):
    # Delete Item
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    # Save new item
    todo_list = Todo.objects.order_by('-hits')
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form, 'todo':todo}

    return render(request,'todo/edit_form.html',context)

def saveTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def deleteTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
