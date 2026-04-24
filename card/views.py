from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Card
from .serializers import CardSerializer


class CardListCreateView(ListCreateAPIView):
    ''' список карточек
'''
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardDetailView(RetrieveUpdateDestroyAPIView):
    '''Только свои карточки
'''
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class TodayCardsView(ListAPIView):
    '''Только текущий пользователь
'''
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user, is_due=True)
