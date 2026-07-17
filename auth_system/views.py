from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from .form import RegisterForm, LoginForm
from .mixins import HiMessageMixin



# Create your views here.
class RegisterView(HiMessageMixin,CreateView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("tasks:task_list")
    success_message = "You have successfully registered. Welcome!"
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
class LogoutView(HiMessageMixin,LogoutView):
    next_page = reverse_lazy("tasks:task_list")
    success_message = "You have been logged out."
class LoginView(HiMessageMixin,LoginView):
    template_name = "auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("tasks:task_list")
    success_message = "You have been logged in."