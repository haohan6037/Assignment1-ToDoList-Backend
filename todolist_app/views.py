from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from todolist_app.serializers import UserSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
