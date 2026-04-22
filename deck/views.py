from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Deck
from .serializers import DeckSerializer


class DeckListCreateView(ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

