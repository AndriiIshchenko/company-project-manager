from django.urls import path

from .views import ProjectActiveListView, ProjectDetailView

urlpatterns = [
    path("", ProjectActiveListView.as_view(), name="index"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
app_name = "project_manager"
