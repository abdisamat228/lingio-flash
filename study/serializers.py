from rest_framework import serializers

from .models import StudySession


class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = ['id', 'user', 'started_at', 'finished_at']
        read_only_fields = ['id', 'user', 'started_at']
