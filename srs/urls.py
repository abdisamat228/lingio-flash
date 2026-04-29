from django.urls import path
from .views import SRSStateListView, CardScheduleView
urlpatterns = [
    path('tts/', SRSStateListView.as_view()),
    path('tts/{card_id}/', CardScheduleView.as_view()),
]