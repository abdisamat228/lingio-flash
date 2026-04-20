from rest_framework import serializers
from .models import StatsOverview

class StatsOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsOverview
        fields = '__all__'