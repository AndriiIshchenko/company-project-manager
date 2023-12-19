from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from project_manager.forms import TaskForm

from project_manager.models import Project, Task

# Create your views here.
# @login_required()
# def index(request):
#     return render(request, "pages/index.html")


class ProjectActiveListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project_completed_list"
    template_name = "pages/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Project.objects.filter(is_complited=False)
        return queryset


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "pages/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "pages/task_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context["status"] = 75
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskForm


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskForm
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TaskCreateView, self).get_context_data(**kwargs)# project_id = 
        a = self.request.POST.get("project_id", "")
        context["form"] = TaskForm(initial={"project": a })
        context["project_id"] = a
        # DriverNameSearchForm(initial={"name": name})
        return context
