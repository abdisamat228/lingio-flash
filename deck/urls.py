from django.urls import path
from .views import DeckListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('decks/',DeckListCreateView.as_view()),
    path('decks/<int:id>/',RetrieveUpdateDestroyView.as_view()),

]