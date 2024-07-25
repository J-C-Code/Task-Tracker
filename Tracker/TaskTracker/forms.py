from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_due']
        widgets = {
            'task_due': forms.DateInput(attrs={'type': 'date'}),
        }
