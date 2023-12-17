# Generated by Django 5.0 on 2023-12-17 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_manager", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Projaect",
        ),
        migrations.RemoveField(
            model_name="project",
            name="tasks",
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="project_manager.project",
            ),
        ),
    ]