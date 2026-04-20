from rest_framework import serializers
from .models import Review

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'User', 'card', 'quality', 'reviewed_at']