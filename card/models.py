from django.db import models

from deck.models import Deck


class Card(models.Model):
    '''Карточка — это контейнер для пары'''
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='cards/', blank=True, null=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.question
