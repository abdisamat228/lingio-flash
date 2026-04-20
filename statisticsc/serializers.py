from rest_framework import serializers


class StatsOverviewSerializer(serializers.Serializer):
    total_decks = serializers.IntegerField()
    total_cards = serializers.IntegerField()
    due_cards = serializers.IntegerField()
    reviewed_today = serializers.IntegerField()


class DailyStatsSerializer(serializers.Serializer):
    date = serializers.DateField()
    reviewed = serializers.IntegerField()
    correct = serializers.IntegerField()


class CardStatsSerializer(serializers.Serializer):
    card = serializers.IntegerField()
    reviews = serializers.IntegerField()
    average_quality = serializers.FloatField()
