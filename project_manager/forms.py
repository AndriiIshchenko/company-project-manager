from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from project_manager.models import Task


class TaskForm(forms.ModelForm):
    assigness = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Workers"
    )

    class Meta:
        model = Task
        fields = "__all__"