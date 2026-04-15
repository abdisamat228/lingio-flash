from django.contrib.auth.models import User
from django.db import models

from english.card.models import Card


# Create your models here.



class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    quality = models.IntegerField()
    reviewed_at = models.ForeignKey(Review, on_delete=models.CASCADE)
