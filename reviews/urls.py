from django.urls import path
from .views import ReviewListView, ReviewAnswerView, NextReviewCardView
urlpatterns = [
    path('/api/v1/review/', ReviewListView.as_view()),
    path('/api/v1/review/answer/', ReviewAnswerView.as_view()),
    path('/api/v1/review/next/', NextReviewCardView.as_view()),
    path('/api/v1/cards/{id}/schedule/', NextReviewCardView.as_view()),
    path('/api/v1/review/answer/', ReviewAnswerView.as_view()),
]