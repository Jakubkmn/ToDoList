from django.utils import timezone
from django.db import models


def one_week():
    return timezone.now() + timezone.timedelta(days=7)

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):

class ToDoItem(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week) 
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    # def get_absolute_url(self):