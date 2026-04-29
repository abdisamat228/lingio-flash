from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import SRSState
from .serializers import SRSStateSerializer


class SRSStateListView(ListAPIView):
    serializer_class = SRSStateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SRSState.objects.filter(user=self.request.user).select_related('card').order_by('next_review')


class CardScheduleView(ListAPIView):
    serializer_class = SRSStateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SRSState.objects.filter(user=self.request.user, card_id=self.kwargs['card_id']).select_related('card')
