from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Deck
from .serializers import DeckSerializer


class DeckListCreateView(ListCreateAPIView):
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeckDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)
