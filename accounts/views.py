
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView


from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    '''Создание пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    '''Аутентификация пользователя'''
    permission_classes = [IsAuthenticated]

class LogoutView(APIView):
    '''Завершение сессии'''
    permission_classes = [IsAuthenticated]

class MeView(APIView):
    '''Возвращает текущего пользователя'''
    permission_classes = [IsAuthenticated]

