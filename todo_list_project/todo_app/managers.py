from django.db import models


class TaskQueryset(models.QuerySet):
    def completed_tasks(self):
        return self.filter(completed=True)

    def uncompleted_tasks(self):
        return self.filter(completed=False).order_by('due_date')