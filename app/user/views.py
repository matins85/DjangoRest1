# from django.shortcuts import render
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
from user.serializers import UserSerializer
from rest_framework import generics
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    