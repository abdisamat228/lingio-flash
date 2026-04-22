from django.urls import path
from .views import DeckListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('/api/decks',DeckListCreateView.as_view()),
    path('/api/decks',DeckListCreateView.as_view()),
    path('/api/decks/{id}',RetrieveUpdateDestroyView.as_view()),
    path('/api/decks/{id}',RetrieveUpdateDestroyView.as_view()),
]