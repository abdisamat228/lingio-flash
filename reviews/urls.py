from django.urls import path
from .views import ReviewListView, ReviewAnswerView, NextReviewCardView
urlpatterns = [
    path('reviews/', ReviewListView.as_view()),
    path('reviews/answer/', ReviewAnswerView.as_view()),
    path('reviews/next/', NextReviewCardView.as_view()),
]
