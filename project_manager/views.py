from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from project_manager.forms import (
    ProjectForm,
    TaskForm,
    WorkerCreationForm,
    WorkerNameSearchForm,
)

from project_manager.models import Project, Task, Worker


class ProjectActiveListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project_active_list"
    template_name = "pages/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Project.objects.filter(is_completed=False).prefetch_related("tasks")
        return queryset


class ProjectCompletedListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project_completed_list"
    template_name = "pages/project_completed.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Project.objects.filter(is_completed=True).prefetch_related("tasks")
        return queryset


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "pages/project_detail.html"
    queryset = Project.objects.all().prefetch_related("tasks")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "pages/project_form.html"
    success_url = reverse_lazy("project_manager:index")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "pages/task_detail.html"
    queryset = Task.objects.all().prefetch_related("assigness")
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("project_manager:index")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy(
            "project_manager:project-detail", kwargs={"pk": self.object.project_id}
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        project_id = self.request.POST.get("project_id", "")
        context["form"] = TaskForm(initial={"project": project_id})
        return context


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "pages/workers_list.html"
    paginate_by = 3

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = WorkerNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Worker.objects.all()
        form = WorkerNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["name"])
        return queryset


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "pages/worker_form.html"
    success_url = reverse_lazy("project-manager:worker-list")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "pages/worker_detail.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    template_name = "pages/worker_form.html"
    form_class = WorkerCreationForm
    success_url = reverse_lazy("project-manager:worker-list")
