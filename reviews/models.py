from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from card.models import Card


# Create your models here.



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='reviews')
    quality = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} reviewed {self.card}'
