from django.shortcuts import render, redirect, get_object_or_404

from todo_list_project.todo_app.forms import TaskAddForm, TaskEditForm, TaskDeleteForm
from todo_list_project.todo_app.models import Task


# Create your views here.
def index(request):
    uncompleted_tasks = Task.objects.uncompleted_tasks()
    completed_tasks = Task.objects.completed_tasks()

    context = {
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
    }

    return render(request, 'index.html', context)


def task_create(request):
    if request.method == 'GET':
        form = TaskAddForm(None)
    else:
        form = TaskAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'task_form.html', context)


def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        form = TaskEditForm(instance=task)
    else:
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'task_form.html', context)


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        form = TaskDeleteForm(instance=task)
    else:
        task.delete()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'delete_task.html', context)
