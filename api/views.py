from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BotUser, Feedback, Filial, FilialDetail
from .serializers import BotUserSerializer, FeedbackSerializer, FilialSerializer, FilialDetailSerializer


class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class FilialDetailViewSet(viewsets.ModelViewSet):
    queryset = FilialDetail.objects.all()
    serializer_class = FilialDetailSerializer
