from django.urls import path

from project_manager.views import (
    ProjectActiveListView,
    ProjectDetailView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView
)

urlpatterns = [
    path("", ProjectActiveListView.as_view(), name="index"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/cretate/", TaskCreateView.as_view(), name="task-create"),
]
app_name = "project_manager"
