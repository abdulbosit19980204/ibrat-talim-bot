from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer


class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
