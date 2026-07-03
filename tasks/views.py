from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
class TaskListView(ListView):
    model = Task
    template_name = 'base.html'
    context_object_name = 'tasks'
    ordering = ['priority']
class TaskDetailView(DetailView):
    model = Task
    template_name = 'base2.html'
    context_object_name = 'tasks'
