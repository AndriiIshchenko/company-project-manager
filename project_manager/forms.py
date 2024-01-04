from datetime import date
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from project_manager.models import Project, Task, Worker


class DateValidationMixin:
    def clean_deadline(self) -> str:
        now = date.today()
        deadline = self.cleaned_data["deadline"]
        if deadline < now:
            raise ValidationError(
                ["The time machine hasn't yet been invented. So 'Deadline' must be in future.",
                f"Today is {now}"]
            )
        return deadline

class TaskForm(forms.ModelForm):
    assigness = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Workers",
    )

    class Meta:
        model = Task
        widgets = {"project": forms.HiddenInput()}
        fields = "__all__"


class ProjectForm(DateValidationMixin, forms.ModelForm):
    assigness = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.filter(position__name__icontains="project manager")
    )

    class Meta:
        model = Project
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )
