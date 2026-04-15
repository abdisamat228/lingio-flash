from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = models.IntegerField()
    quality = models.IntegerField()
    reviewed_at = models.DateTimeField()