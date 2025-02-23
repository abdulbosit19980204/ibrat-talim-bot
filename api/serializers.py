from rest_framework import serializers
from api.models import Feedback, BotUser, Filial, FilialDetail, Fanlar, Yonalishlar, Price, Chegirmalar


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


class FanlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = ['name']


class YonalishlarSerializer(serializers.ModelSerializer):
    fanlar = FanlarSerializer(many=True, read_only=True)  # Yo'nalishga tegishli fanlarni olish

    class Meta:
        model = Yonalishlar
        fields = ['name', 'fanlar']


class PriceSerializer(serializers.ModelSerializer):
    fan = FanlarSerializer(many=False, read_only=True)

    class Meta:
        model = Price
        fields = ['fan', 'price', 'comment']


class ChegirmaSerializer(serializers.ModelSerializer):
    fan = FanlarSerializer(many=True, read_only=True)

    class Meta:
        model = Chegirmalar
        fields = ['name', 'miqdori', 'started_at', 'ended_at', 'fan', 'is_foiz', 'is_miqdor']
        depth = 1
