from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import SRSState
from .serializers import SRSStateSerializer



class SRSStateListView(ListAPIView):
    '''возвращает интервал'''
    serializer_class = SRSStateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SRSState.objects.filter(user=self.request.user)

class CardScheduleView(ListAPIView):
    '''возвращает повторения'''
    serializer_class = SRSStateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SRSState.objects.filter(user=self.request.user)
