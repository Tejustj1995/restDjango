from django.shortcuts import render
from .models import Songs
from .serializers import SongsSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ListSongsView(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
