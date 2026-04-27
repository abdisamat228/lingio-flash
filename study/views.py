from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import StudySession
from .serializers import StudySessionSerializer

class StudySessionStartView(APIView):
    '''Следующая карточка'''
    permission_classes = [IsAuthenticated]

class StudyNextCardView(APIView):
    '''Если нет → сообщение'''
    permission_classes = [IsAuthenticated]

class StudySessionFinishView(APIView):
    '''изучает сессию'''
    permission_classes = [IsAuthenticated]

