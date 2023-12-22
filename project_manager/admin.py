from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Task, TaskType, Worker, Position, Project


admin.site.register(Position)
admin.site.register(TaskType)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline")


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )
