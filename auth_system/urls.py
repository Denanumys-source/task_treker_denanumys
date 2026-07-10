from django.shortcuts import render
from django.urls import path,include,reverse_lazy
from .views import RegisterView,LoginView,LogoutView
urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(success_url=reverse_lazy('auth_system:login')),name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('tasks:task_list')),name='logout'),
]

app_name = 'auth_system'