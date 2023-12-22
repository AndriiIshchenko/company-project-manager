from django import template

from project_manager.models import Project, Task

register = template.Library()


@register.filter
def completed_task(instnce: [Task, Project], status: bool) -> int:
    """Returns amount of completed or not Tasks and Projects"""
    amount = (
        instnce.tasks.filter(is_completed=status).count()
        + instnce.projects.filter(is_completed=status).count()
    )
    return amount


@register.filter
def worker_amount(instance: Project) -> int:
    """Returns amount of assigness of all tasks of project"""
    amount = 0
    tasks = instance.tasks.all()
    for task in tasks:
        amount += task.assigness.count()

    amount += instance.assigness.count()
    return amount
