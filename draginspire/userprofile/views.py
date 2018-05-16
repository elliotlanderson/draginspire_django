from django.contrib.auth.models import User
from rest_framework import viewsets
from draginspire.userprofile.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    