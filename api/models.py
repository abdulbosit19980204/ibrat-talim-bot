from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class BotUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Filial(models.Model):  # models.Model qayta yozilmaydi
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='filial_author', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FilialDetail(models.Model):
    filial = models.OneToOneField(Filial, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='filial_detail_author', on_delete=models.CASCADE)
    description = models.TextField()
    rasm_file = models.ImageField(upload_to="rasm")
    rasm = models.CharField(max_length=500,
                            default="https://avatars.mds.yandex.net/get-altay/5476806/2a00000180c6aee71376d9aea3dc55862bd0/L_height")
    manzil = models.CharField(max_length=355)

    def __str__(self):
        return self.filial.name


class Yonalishlar(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='yonalish_author', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Fanlar(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='filials', on_delete=models.CASCADE)

    yonalishlar = models.ForeignKey(Yonalishlar, on_delete=models.SET_NULL, null=True, related_name="fanlar")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    fan = models.ForeignKey(Fanlar, on_delete=models.SET_NULL, null=True, related_name="price")
    author = models.ForeignKey(User, related_name='price_author', on_delete=models.CASCADE)

    price = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fan.name


class Chegirmalar(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='chegirma_author', on_delete=models.CASCADE)
    fan = models.ManyToManyField(Fanlar, null=True, related_name="chegirma")
    is_foiz = models.BooleanField(default=True)
    is_miqdor = models.BooleanField(default=False)
    miqdori = models.FloatField(default=0)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user_id = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
