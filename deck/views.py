from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Deck
from .serializers import DeckSerializer


class DeckListCreateView(ListCreateAPIView):
    '''список колод пользователя
'''
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''Получение / обновление / удаление
'''
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

