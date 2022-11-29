from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank = True)
    created_date = models.DateTimeField(auto_now_add=True)