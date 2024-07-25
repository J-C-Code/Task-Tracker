from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_complete = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.BigAutoField(primary_key=True)
    task_due = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name