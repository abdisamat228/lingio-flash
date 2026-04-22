from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import SRS
from .serializers import SRSSerializer
from ..deck.models import Deck


class SRSStateListView(ListAPIView):
    queryset = SRS.objects.all()
    serializer_class = SRSSerializer
    permission_classes = [IsAuthenticated]

class CardScheduleView(ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

