from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema


User = get_user_model()

@extend_schema(
    request=RegisterSerializer,
    responses={201:RegisterSerializer},
    description="Register new user",
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer