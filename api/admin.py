from django.contrib import admin
from api.models import BotUser, Feedback, Filial, FilialDetail, Yonalishlar, Fanlar, Price, Chegirmalar
from ckeditor.widgets import CKEditorWidget
from django.db import models


class RichTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget()},  # RichText qo‘shish
    }


class BotUserDataAdmin(admin.ModelAdmin):
    model = BotUser
    list_display = ('id', 'name', 'surname', 'username', 'user_id', 'phone_number')
    list_display_links = ('id', 'name', 'username', 'phone_number')
    search_fields = ('phone_number', 'username', 'name', 'surname')
    list_filter = ('phone_number',)
    fieldsets = (
        ('Client Info', {'fields': ('name', 'surname', 'phone_number',)}),
        ('Telegram Info', {'fields': ('user_id', 'username')}),
    )


class FilialDataAdmin(admin.ModelAdmin):
    model = Filial
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name',)


class FililaDetailDataAdmin(admin.ModelAdmin):
    model = FilialDetail
    list_display = ('id', 'filial__name', 'author__username', 'manzil')
    list_display_links = ('id', 'filial__name',)
    search_fields = ('filial__name', 'manzil',)
    list_filter = ('filial__name',)
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget()},  # RichText qo‘shish
    }


class YonalishlarDataAdmin(admin.ModelAdmin):
    model = Yonalishlar
    list_display = ('id', 'name', 'author__username', 'created_at',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'author__username',)
    list_filter = ('created_at',)


class FanlarDataAdmin(admin.ModelAdmin):
    model = Fanlar
    list_display = ('id', 'name', 'author__username', 'is_active', 'created_at')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'author__username', 'is_active',)
    list_filter = ('is_active',)


class PriceDataAdmin(admin.ModelAdmin):
    model = Price
    list_display = ('id', 'fan__name', 'price', 'author__username', 'created_at', 'is_active')
    list_display = ('id', 'fan__name', 'price')
    search_fields = ('fan__name', 'price',)
    list_filter = ('created_at',)
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget()},  # RichText qo‘shish
    }


admin.site.register(BotUser, BotUserDataAdmin)
admin.site.register(Feedback)
admin.site.register(Filial, FilialDataAdmin)
admin.site.register(FilialDetail, FililaDetailDataAdmin)
admin.site.register(Yonalishlar, YonalishlarDataAdmin)
admin.site.register(Fanlar, FanlarDataAdmin)
admin.site.register(Price, PriceDataAdmin)
admin.site.register(Chegirmalar)
