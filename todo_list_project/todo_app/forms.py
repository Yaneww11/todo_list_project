from django import forms

from todo_list_project.todo_app.models import Task


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Task description'}),
            'due_date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''


class TaskAddForm(BaseTaskForm):
    pass


class TaskEditForm(BaseTaskForm):
    pass


class TaskDeleteForm(BaseTaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
