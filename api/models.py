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
    rasm_file = models.ImageField(upload_to="rasm")
    rasm = models.TextField(
        default="https://avatars.mds.yandex.net/get-altay/5476806/2a00000180c6aee71376d9aea3dc55862bd0/L_height")
    manzil = models.CharField(max_length=255)

    def __str__(self):
        return self.filial.name


# YONALISHLAR = {
#     "🗣Xorijiy Tillar": ["🏴󠁧󠁢󠁥󠁮󠁧󠁿Ingiliz", "🇷🇺Rus", "🇰🇷Koreys", "🇩🇪Nemis"],
#     "📚Aniq Fanlar": ["➕Matematika", "⚡Fizika"],
#     "📚Tabiy Fanlar": ["🧪Kimyo", "🐍Biologiya"],
#     "💻Zamonaviy Fanlar": ["Kompyuter Savodxonligi", "Mobilografiya | SMM", "Grafik Dizayn", "Dasturlash"]
# }

class Yonalishlar(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Fanlar(models.Model):
    name = models.CharField(max_length=255)
    yonalishlar = models.ForeignKey(Yonalishlar, on_delete=models.SET_NULL, null=True, related_name="fanlar")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user_id = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
