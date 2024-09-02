from django import forms
from models import Task


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Task description'}),
            'due_date': forms.URLInput(attrs={'placeholder': 'Task expiration date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''


class TaskAddForm(BaseTaskForm):
    class Meta:
        fields = ['title', 'description', 'due_date']


class TaskEditForm(BaseTaskForm):
    pass


class TaskDeleteForm(BaseTaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
