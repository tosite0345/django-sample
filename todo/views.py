from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Task

def sample(request):
    return HttpResponse('it works')

def sample_view(request):
    context = {}
    return render(request, 'todo/sample.html', context)

def index(request):
    context = { 'tasks': Task.objects.all }
    return render(request, 'todo/index.html', context)

def new(request):
    context = { 'tasks': Task.objects.all }
    return render(request, 'todo/new.html', context)

def create(request):
    p = request.POST
    task = Task.objects.create(name=p['name'], state=p['state'])
    return redirect('/todo')

def edit(request, task_id):
    context = { 'task': Task.objects.get(pk=task_id) }
    return render(request, 'todo/edit.html', context)

def update(request, task_id):
    p = request.POST
    task = Task.objects.get(pk=task_id)
    task.name = p['name']
    task.state = p['state']
    task.save()
    return redirect('/todo')

def delete(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return redirect(request.META['HTTP_REFERER'])
