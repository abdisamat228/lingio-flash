from rest_framework import serializers


class StatsOverviewSerializer(serializers.Serializer):
    '''это «аналитический фильтр»'''
    total_decks = serializers.IntegerField()
    total_cards = serializers.IntegerField()
    due_cards = serializers.IntegerField()
    reviewed_today = serializers.IntegerField()


class DailyStatsSerializer(serializers.Serializer):
    '''это «микроскоп» для твоих достижений за конкретный день'''
    date = serializers.DateField()
    reviewed = serializers.IntegerField()
    correct = serializers.IntegerField()


class CardStatsSerializer(serializers.Serializer):
    '''это «диагностическая карта» конкретной карточки'''
    card = serializers.IntegerField()
    reviews = serializers.IntegerField()
    average_quality = serializers.FloatField()
