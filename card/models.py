from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()

    deck = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='cards'
    )

    def str(self):
        return self.question
