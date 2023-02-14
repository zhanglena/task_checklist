from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from projects.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    # success_url = reverse_lazy("list_projects")

    def get_queryset(self):
        projects = Project.objects.filter(members=self.request.user)
        return projects


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]
    # success_url = reverse_lazy("show_project")

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])

    # def form_valid(self, form):
    #     form.instance.members.set() == self.request.user
    #     return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_queryset(self, **kwargs):
        return Project.objects.filter(members=self.request.user)
