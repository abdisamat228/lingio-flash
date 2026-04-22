from django.urls import path
from .views import SRSStateListView, CardScheduleView
urlpatterns = [
    path('/api/v1/tts/', SRSStateListView.as_view()),
    path('/api/v1/tts/{card_id}/', CardScheduleView.as_view()),
]