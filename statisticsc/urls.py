from django.urls import path

from .views import CardStatsView, DailyStatsView, StatsOverviewView

urlpatterns = [
    path('stats/overview/', StatsOverviewView.as_view()),
    path('stats/daily/', DailyStatsView.as_view()),
    path('stats/cards/', CardStatsView.as_view()),
]
