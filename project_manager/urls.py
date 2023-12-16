from django.urls import path

from .views import ProjectComletedListView

urlpatterns = [
    path("", ProjectComletedListView.as_view(), name="index"),
]
app_name = "project_manager"
