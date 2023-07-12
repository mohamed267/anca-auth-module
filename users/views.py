from django.shortcuts import render

from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from .serializers import RegisterUserSerialier
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.


class RegisterUserView(CreateAPIView):
    queryset =  get_user_model().objects.all()
    permission_classes = { AllowAny }
    serializer_class =  RegisterUserSerialier

