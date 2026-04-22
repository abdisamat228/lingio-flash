from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Study
from .serializers import StudySerializer

class StudySessionStartView(APIView):
    permission_classes = [IsAuthenticated]

class StudyNextCardView(APIView):
    permission_classes = [IsAuthenticated]

class StudySessionFinishView(APIView):
    permission_classes = [IsAuthenticated]
