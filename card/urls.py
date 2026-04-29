from django.urls import path

from .views import CardListCreateView, CardDetailView, TodayCardsView

urlpatterns = [
    path('cards/', CardListCreateView.as_view()),
    path('cards?tag=food/', CardListCreateView.as_view()),
    path('cards/today/', TodayCardsView.as_view()),
    path('decks/<int:id>/copy/', CardDetailView.as_view()),
    path('decks/<int:id>/gr/', CardDetailView.as_view()),
    path('media/upload/', TodayCardsView.as_view()),
]
