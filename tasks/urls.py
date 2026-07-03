from django.shortcuts import render
from django.urls import path,include
from .views import TaskListView,TaskDetailView
urlpatterns = [
    path('', TaskListView.as_view(),name='task_list'),
    path('/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]