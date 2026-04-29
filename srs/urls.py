from django.urls import path
from .views import SRSStateListView, CardScheduleView
urlpatterns = [
    path('srs/', SRSStateListView.as_view()),
    path('cards/<int:card_id>/schedule/', CardScheduleView.as_view()),
]
