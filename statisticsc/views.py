from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Statistics
from .serializers import StatisticsSerializer

class StatsOverviewView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [IsAuthenticated]

class DailyStatsView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [IsAuthenticated]

class CardStatsView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [IsAuthenticated]

