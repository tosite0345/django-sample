from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name  = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
