from django.db import models

from deck.models import Deck


class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.question
