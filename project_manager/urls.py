from django.urls import path

from project_manager.views import (
    ProjectActiveListView,
    ProjectCreateView,
    ProjectDetailView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    WorkerListView,
    WorkerCreateView,
    WorkerDetailView
)

urlpatterns = [
    path("", ProjectActiveListView.as_view(), name="index"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/cretate/", TaskCreateView.as_view(), name="task-create"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]
app_name = "project_manager"
