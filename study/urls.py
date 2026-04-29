from django.urls import path
from .views import StudySessionStartView, StudyNextCardView,StudySessionFinishView
urlpatterns = [
    path('study/session/',StudySessionStartView.as_view()),
    path('study/next/', StudyNextCardView.as_view()),
    path('study/finish/', StudySessionFinishView.as_view()),
]