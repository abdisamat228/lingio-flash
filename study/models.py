from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class StudySession(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
