from django.urls import path
from .views import DeckDetailView, DeckListCreateView

urlpatterns = [
    path('decks/', DeckListCreateView.as_view()),
    path('decks/<int:id>/', DeckDetailView.as_view()),
]
