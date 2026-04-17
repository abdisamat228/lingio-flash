from django.urls import path
urlpatterns = [
    path('/api/cards'),
    path('/api/cards?tag=food'),
    path('/api/cards/today'),
    path('/api/decks/{id}/copy'),
    path('/api/decks/{id}/gr'),
    path('/api/media/upload'),
]