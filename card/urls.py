from django.urls import path

from .views import CardListCreateView, CardDetailView, TodayCardsView

urlpatterns = [
    path('cards/', CardListCreateView.as_view()),
    path('cards/today/', TodayCardsView.as_view()),
    path('cards/<int:id>/', CardDetailView.as_view()),
]
