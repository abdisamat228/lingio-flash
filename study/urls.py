from django.urls import path
from .views import StudyNextCardView, StudySessionFinishView, StudySessionStartView
urlpatterns = [
    path('study/session/', StudySessionStartView.as_view()),
    path('study/next/', StudyNextCardView.as_view()),
    path('study/finish/', StudySessionFinishView.as_view()),
]
