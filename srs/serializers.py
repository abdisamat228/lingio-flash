from rest_framework import serializers
from .models import SRSState

class SRSStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRSState
        fields = ['id', 'User', 'card', 'interval', 'ease_factor', 'repetitions', 'next_review', 'updated_at']
