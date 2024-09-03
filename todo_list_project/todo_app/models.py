from django.db import models

from todo_list_project.todo_app.managers import TaskQueryset


# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    completed = models.BooleanField(default=False)

    due_date = models.DateField(
        null=True,
        blank=True
    )

    objects = TaskQueryset().as_manager()

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
