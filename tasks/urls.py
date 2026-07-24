from django.shortcuts import render
from django.urls import path,include,reverse_lazy
from .views import TaskDeleteView, TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,CommentCreateView,CommentDeleteView,CommentUpdateView,CommentListView,CommentLike
urlpatterns = [
    path('', TaskListView.as_view(),name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/comment/', CommentListView.as_view(), name='comment_list'),
    path('<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/comment/delete/<int:com_pk>', CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:pk>/comment/update/<int:com_pk>', CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/comment/like/<int:com_pk>', CommentLike.as_view(), name='comment_like'),
    
]

app_name = 'tasks'