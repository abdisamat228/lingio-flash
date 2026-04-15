from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

