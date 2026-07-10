from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import TaskForm, CommentForm
from .mixins import PermissionDenied, UserIsOwnerMixin,HiMessageMixin
from .models import Task, Comment


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("-created_at")
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = self.object
            comment.save()
        return redirect("tasks:task_detail", pk=self.object.pk)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("tasks:task_list")


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_update.html"
    success_url = reverse_lazy("tasks:task_list")
    context_object_name = "tasks"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = f'Update Task: {self.object.title}'
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")
    template_name = "tasks/task_delete.html"
    context_object_name = "tasks"



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/comment_create.html"

class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "tasks/comment_form.html"
    success_url = reverse_lazy("tasks:comment_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "tasks/comment_form.html"

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.task.pk})

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "tasks/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.task.pk})

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
