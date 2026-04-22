from django.urls import path
from .views import StudySessionStartView, StudyNextCardView
urlpatterns = [
    path('/api/v1/study/session/',StudySessionStartView.as_view()),
    path('/api/v1/study/next/', StudyNextCardView.as_view()),
    path('/api/v1/study/finish/', StudySessionFinishView.as_view()),
]