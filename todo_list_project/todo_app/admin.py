from django.contrib import admin

from todo_list_project.todo_app.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed')
    list_filter = ('due_date',)
    search_fields = ('title',)
