# Generated by Django 5.0 on 2023-12-21 18:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project_manager", "0002_delete_projaect_remove_project_tasks_task_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="is_complited",
            new_name="is_completed",
        ),
    ]
