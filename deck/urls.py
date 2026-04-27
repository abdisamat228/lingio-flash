from django.urls import path
from .views import DeckListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('/api/decks',DeckListCreateView.as_view()),
    path('/api/decks/<int:id>',RetrieveUpdateDestroyView.as_view()),

]