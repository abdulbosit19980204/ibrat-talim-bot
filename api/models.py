from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Filial(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FilialDetail(models.Model):
    filial = models.OneToOneField(Filial, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to="rasm")
    manzil = models.CharField(max_length=255)


class Feedback(models.Model):
    user_id = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
