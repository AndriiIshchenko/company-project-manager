from asyncio import Task
from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from project_manager.models import Project

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


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "pages/task_detail.html"
