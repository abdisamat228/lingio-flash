from django.utils import timezone
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from srs.models import SRSState

from .models import Card
from .serializers import CardSerializer


class CardListCreateView(ListCreateAPIView):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Card.objects.filter(deck__user=self.request.user).select_related('deck')
        deck_id = self.request.query_params.get('deck')
        if deck_id:
            queryset = queryset.filter(deck_id=deck_id)
        return queryset

    def perform_create(self, serializer):
        deck = serializer.validated_data['deck']
        if deck.user != self.request.user:
            raise PermissionDenied('You can only add cards to your own decks.')
        serializer.save()


class CardDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Card.objects.filter(deck__user=self.request.user).select_related('deck')


class TodayCardsView(ListAPIView):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        due_card_ids = list(
            SRSState.objects.filter(
            user=self.request.user,
            next_review__lte=timezone.now(),
            ).values_list('card_id', flat=True)
        )
        if due_card_ids:
            return Card.objects.filter(id__in=due_card_ids, deck__user=self.request.user).select_related('deck')
        return Card.objects.filter(deck__user=self.request.user).select_related('deck')[:10]
