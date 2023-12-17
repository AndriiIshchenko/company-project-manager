from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="workers"
    )

    def __str__(self):
        return f"{self.username} {self.position}"


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    is_complited = models.BooleanField(default=False)

    assigness = models.ManyToManyField(Worker, related_name="projects")

    def __str__(self):
        return f"{self.name} {self.deadline}"


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    is_complited = models.BooleanField(default=False)
    TASK_PRIORITY_CHOICE = (
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Normal", "Normal"),
        ("Low", "Low"),
    )
    priority = models.CharField(
        max_length=20,
        choices=TASK_PRIORITY_CHOICE,
        default="Normal",
    )
    task_type = models.ForeignKey(
        TaskType, related_name="tasks", on_delete=models.DO_NOTHING
    )
    assigness = models.ManyToManyField(Worker, related_name="tasks")
    project = models.ForeignKey(
            Project,
            related_name="tasks",
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )

    def __str__(self):
        return f"{self.name} {self.priority}"
