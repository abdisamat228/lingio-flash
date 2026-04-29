from django.db.models import Avg, Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from card.models import Card
from deck.models import Deck
from reviews.models import Review
from srs.models import SRSState

from .serializers import CardStatsSerializer, DailyStatsSerializer, StatsOverviewSerializer


class StatsOverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = {
            'total_decks': Deck.objects.filter(user=request.user).count(),
            'total_cards': Card.objects.filter(deck__user=request.user).count(),
            'due_cards': SRSState.objects.filter(user=request.user, next_review__lte=timezone.now()).count(),
            'reviewed_today': Review.objects.filter(user=request.user, reviewed_at__date=timezone.localdate()).count(),
        }
        return Response(StatsOverviewSerializer(payload).data)


class DailyStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rows = (
            Review.objects.filter(user=request.user)
            .annotate(date=TruncDate('reviewed_at'))
            .values('date')
            .annotate(reviewed=Count('id'), average_quality=Avg('quality'))
            .order_by('-date')[:14]
        )
        payload = [{'date': row['date'], 'reviewed': row['reviewed'], 'correct': row['reviewed']} for row in rows]
        return Response(DailyStatsSerializer(payload, many=True).data)


class CardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rows = (
            Review.objects.filter(user=request.user)
            .values('card')
            .annotate(reviews=Count('id'), average_quality=Avg('quality'))
            .order_by('-reviews')
        )
        return Response(CardStatsSerializer(rows, many=True).data)
