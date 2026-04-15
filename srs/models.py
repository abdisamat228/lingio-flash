from django.db import models

from english.reviews.models import Review


# Create your models here.


class SRSState(models.Model):
    card_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    interval = models.IntegerField()
    ease_factor = models.IntegerField()
    repetitions = models.IntegerField()
    next_review = models.DateTimeField()
    updated_at = models.DateTimeField()