from django.shortcuts import render
from django.urls import path,include,reverse_lazy
from .views import TaskDeleteView, TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,CommentCreateView,CommentDeleteView,CommentUpdateView
urlpatterns = [
    path('', TaskListView.as_view(),name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
]

app_name = 'tasks'