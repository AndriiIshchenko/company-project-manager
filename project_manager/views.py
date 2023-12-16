from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
