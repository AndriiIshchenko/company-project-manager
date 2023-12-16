from django.urls import path

from .views import ProjectActiveListView

urlpatterns = [
    path("", ProjectActiveListView.as_view(), name="index"),
]
app_name = "project_manager"
