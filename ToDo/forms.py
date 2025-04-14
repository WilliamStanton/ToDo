from django.forms import ModelForm

from ToDo.models import Task

# Define forms
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'completed']