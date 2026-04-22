from django.urls import path
from .views import StatsOverviewView, DailyStatsView, CardStatsView
urlpatterns = [
    path('/api/v1/stats/overview', StatsOverviewView.as_view()),
    path('/api/v1/stats/daily/', DailyStatsView.as_view()),
    path('/api/v1/stats/cards/', CardStatsView.as_view()),

]