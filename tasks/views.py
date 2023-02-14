from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    # success_url = reverse_lazy("show_project")

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        tasks = Task.objects.filter(assignee=self.request.user)
        return tasks


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
