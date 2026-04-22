from rest_framework.generics import CardListCreateView, CardDetailView, TodayCardsView
from rest_framework.permissions import IsAuthenticated
from .models import Card
from .serializers import CardSerializer

class CardListCreateView(CardListCreateView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class CardDetailView(CardDetailView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class TodayCardsView(TodayCardsView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]