from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
