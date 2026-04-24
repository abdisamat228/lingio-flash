from django.urls import path

from english.card.views import CardListCreateView, CardDetailView, TodayCardsView

urlpatterns = [
    path('/api/cards', CardListCreateView.as_view()),
    path('/api/cards?tag=food', CardListCreateView.as_view()),
    path('/api/cards/today', TodayCardsView.as_view()),
    path('/api/decks/<int:id>/copy', CardDetailView.as_view()),
    path('/api/decks/<int:id>/gr', CardDetailView.as_view()),
    path('/api/media/upload', TodayCardsView.as_view()),
]
