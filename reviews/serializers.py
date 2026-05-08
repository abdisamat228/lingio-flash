from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    '''Проверяет, существует ли карточка, на которую ты ответил'''
    class Meta:
        model = Review
        fields = ['id', 'user', 'card', 'quality', 'reviewed_at']
        read_only_fields = ['id', 'user', 'reviewed_at']
