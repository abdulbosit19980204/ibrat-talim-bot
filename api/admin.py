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
    list_display = ('id', 'name', 'author__username', 'created_at')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'author__username',)
    list_filter = ('created_at',)


admin.site.register(BotUser, BotUserDataAdmin)
admin.site.register(Feedback)
admin.site.register(Filial)
admin.site.register(FilialDetail, FililaDetailDataAdmin)
admin.site.register(Yonalishlar, YonalishlarDataAdmin)
admin.site.register(Fanlar)
admin.site.register(Price, RichTextAdmin)
admin.site.register(Chegirmalar)
