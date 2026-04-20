from rest_framework import serializers
from .models import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'User', 'Title', 'description', 'is_public', 'created_at']

