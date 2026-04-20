from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from card.models import Card


# Create your models here.


class SRSState(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='srs_states')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='srs_states')
    interval = models.PositiveIntegerField(default=0)
    ease_factor = models.FloatField(default=2.5)
    repetitions = models.PositiveIntegerField(default=0)
    next_review = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'card'], name='unique_srs_state_per_user_card')
        ]

    def __str__(self):
        return f'{self.user} - {self.card}'
