# Generated by Django 5.0 on 2023-12-21 18:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project_manager", "0003_rename_is_complited_task_is_completed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="is_complited",
            new_name="is_completed",
        ),
    ]
