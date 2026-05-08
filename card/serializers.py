from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    '''это сриалайзер для rfhnjxrb'''
    class Meta:
        model = Card
        fields = ['id', 'question', 'answer', 'image', 'deck']
        read_only_fields = ['id']
