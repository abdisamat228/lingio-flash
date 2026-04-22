from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import AccountsSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [IsAuthenticated]

class LoginView(APIView):
    permission_classes = [IsAuthenticated]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

class MeView(APIView):
    permission_classes = [IsAuthenticated]

