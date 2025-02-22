from rest_framework import serializers
from api.models import Feedback, BotUser, Filial, FilialDetail


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'


class FilialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialDetail
        fields = ['description', 'rasm', 'manzil']


class FilialSerializer(serializers.ModelSerializer):
    filial_detail = FilialDetailSerializer(source='filialdetail', read_only=True)

    class Meta:
        model = Filial
        fields = ['name', 'filial_detail']
