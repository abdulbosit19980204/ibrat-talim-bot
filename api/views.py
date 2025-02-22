from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BotUser, Feedback, Filial, FilialDetail, Yonalishlar, Fanlar
from .serializers import BotUserSerializer, FeedbackSerializer, FilialSerializer, FilialDetailSerializer, \
    YonalishlarSerializer, FanlarSerializer


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


class YonalishlarViewSet(viewsets.ModelViewSet):
    """Yo‘nalishlar va ularning fanlarini `dict` formatida qaytaruvchi API"""
    queryset = Yonalishlar.objects.all()
    serializer_class = YonalishlarSerializer

    def list(self, request):
        yonalish_dict = {}
        yonalishlar = Yonalishlar.objects.prefetch_related("fanlar").all()

        for yonalish in yonalishlar:
            fanlar_list = [fan.name for fan in yonalish.fanlar.all()]
            yonalish_dict[yonalish.name] = fanlar_list

        return Response(yonalish_dict)


class FanlarViewSet(viewsets.ModelViewSet):
    queryset = Fanlar.objects.all()
    serializer_class = FanlarSerializer
