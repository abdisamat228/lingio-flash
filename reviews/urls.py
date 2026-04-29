from django.urls import path
from .views import ReviewListView, ReviewAnswerView, NextReviewCardView
urlpatterns = [
    path('review/', ReviewListView.as_view()),
    path('review/answer/', ReviewAnswerView.as_view()),
    path('review/next/', NextReviewCardView.as_view()),
    path('cards/<int:id>/schedule/', NextReviewCardView.as_view()),
    path('review/answer/', ReviewAnswerView.as_view()),
]