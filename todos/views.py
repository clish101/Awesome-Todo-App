from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import NewTodoForm
from django.views.decorators.http import require_POST


def home(request):
    form = NewTodoForm()
    todos = Todo.objects.order_by('-id')
    context = {'todos': todos, 'form': form}
    return render(request, 'todos/index.html', context)


def complete(request, text_pk):
    todo = Todo.objects.get(pk=text_pk)
    todo.completed = True
    todo.save()
    return redirect('home')


@require_POST
def create(request):
    form = NewTodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=form.cleaned_data.get('text'))
        new_todo.save()
        return redirect('home')


def delete(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('home')


def deleteOne(request, todo_pk):
    Todo.objects.filter(pk=todo_pk).delete()
    return redirect('home')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('home')
