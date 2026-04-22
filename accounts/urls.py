from django.urls import path
from .views import RegisterView, LoginView, LogoutView,MeView
urlpatterns = [
    path('/api/v1/auth/register/', RegisterView.as_view()),
    path('/api/v1/auth/login/', LoginView.as_view()),
    path('/api/v1/auth/logout/', LogoutView.as_view()),
    path('/api/v1/auth/me/', MeView.as_view()),



]