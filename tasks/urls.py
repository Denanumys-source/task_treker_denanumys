from django.shortcuts import render
from django.urls import path,include,reverse_lazy
from .views import TaskDeleteView, TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,CommentListView,CommentCreateView,CommentDeleteView,CommentUpdateView,LikeView
urlpatterns = [
    path('', TaskListView.as_view(),name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/comments/<int:com_pk>', CommentListView.as_view(), name='comment_list'),
    path('<int:pk>/comments/like/<int:com_pk>', LikeView, name='like'),
    path('<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/comments/delete/<int:com_pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:pk>/comments/update/<int:com_pk>/', CommentUpdateView.as_view(), name='comment_update'),
]

app_name = 'tasks'