from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from card.models import Card
from card.serializers import CardSerializer
from srs.models import SRSState
from srs.serializers import SRSStateSerializer

from .models import Review
from .serializers import ReviewSerializer


def _update_srs_state(state, quality):
    if quality < 3:
        state.repetitions = 0
        state.interval = 1
    else:
        state.repetitions += 1
        if state.repetitions == 1:
            state.interval = 1
        elif state.repetitions == 2:
            state.interval = 6
        else:
            state.interval = max(1, round(state.interval * state.ease_factor))

    delta = 5 - quality
    state.ease_factor = max(1.3, state.ease_factor + (0.1 - delta * (0.08 + delta * 0.02)))
    state.next_review = timezone.now() + timedelta(days=state.interval)
    state.save()
    return state


class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).select_related('card').order_by('-reviewed_at')


class ReviewAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        card = serializer.validated_data['card']
        if card.deck.user != request.user:
            return Response({'detail': 'Card does not belong to the current user.'}, status=status.HTTP_403_FORBIDDEN)

        review = Review.objects.create(
            user=request.user,
            card=card,
            quality=serializer.validated_data['quality'],
        )
        state, _ = SRSState.objects.get_or_create(user=request.user, card=card)
        state = _update_srs_state(state, review.quality)
        return Response(
            {
                'review': ReviewSerializer(review).data,
                'schedule': SRSStateSerializer(state).data,
            },
            status=status.HTTP_201_CREATED,
        )


class NextReviewCardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        state = (
            SRSState.objects.filter(user=request.user)
            .select_related('card', 'card__deck')
            .order_by('next_review')
            .first()
        )
        if state is None:
            return Response({'detail': 'No cards available for review.'}, status=status.HTTP_200_OK)
        return Response(
            {
                'card': CardSerializer(state.card).data,
                'schedule': SRSStateSerializer(state).data,
            }
        )
