from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

class ReviewListView(ListAPIView):
    '''История повторений'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class ReviewAnswerView(RetrieveUpdateDestroyAPIView):
    '''Проверка принадлежности карточки'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class NextReviewCardView(RetrieveUpdateDestroyAPIView):
    '''Найти ближайшую карточку для повторения
'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


