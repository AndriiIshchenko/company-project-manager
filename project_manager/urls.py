from django.urls import path

from .views import ProjectActiveListView, ProjectDetailView, TaskDetailView

urlpatterns = [
    path("", ProjectActiveListView.as_view(), name="index"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
app_name = "project_manager"
