from django import template

from project_manager.models import Project, Task

register = template.Library()


@register.filter
def complited_task(instnce: [Task,Project], status: bool) -> int:
    """Returns amount of complited or not Tasks and Projects"""
    amount = (
        instnce.tasks.filter(is_complited=status).count()
        + instnce.projects.filter(is_complited=status).count()
    )
    return amount
