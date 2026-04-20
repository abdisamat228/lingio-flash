from rest_framework import serializers

from .models import Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'user', 'title', 'description', 'is_public', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
