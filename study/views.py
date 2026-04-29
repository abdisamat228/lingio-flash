from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from card.models import Card
from card.serializers import CardSerializer
from srs.models import SRSState

from .models import StudySession
from .serializers import StudySessionSerializer


class StudySessionStartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = StudySession.objects.create(user=request.user)
        return Response(StudySessionSerializer(session).data, status=status.HTTP_201_CREATED)


class StudyNextCardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        due_state = (
            SRSState.objects.filter(user=request.user)
            .select_related('card', 'card__deck')
            .order_by('next_review')
            .first()
        )
        if due_state:
            return Response(CardSerializer(due_state.card).data)

        card = Card.objects.filter(deck__user=request.user).select_related('deck').first()
        if card is None:
            return Response({'detail': 'No cards available.'}, status=status.HTTP_200_OK)
        return Response(CardSerializer(card).data)


class StudySessionFinishView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = (
            StudySession.objects.filter(user=request.user, finished_at__isnull=True)
            .order_by('-started_at')
            .first()
        )
        if session is None:
            return Response({'detail': 'No active study session.'}, status=status.HTTP_404_NOT_FOUND)
        session.finished_at = timezone.now()
        session.save(update_fields=['finished_at'])
        return Response(StudySessionSerializer(session).data)
