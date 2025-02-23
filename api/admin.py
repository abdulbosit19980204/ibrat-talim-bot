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
    list_display = ('id', 'first_name', 'last_name', 'username', 'user_id', 'phone_number')
    list_display_links = ('id', 'user_name', 'phone_number')
    search_fields = ('phone_number', 'username', 'first_name', 'last_name')
    list_filter = ('phone_number',)
    fieldsets = (
        ('Client Info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Telegram Info', {'fields': ('user_id', 'username')}),
    )


admin.site.register(BotUser, BotUserDataAdmin)
admin.site.register(Feedback)
admin.site.register(Filial)
admin.site.register(FilialDetail, RichTextAdmin)
admin.site.register(Yonalishlar)
admin.site.register(Fanlar)
admin.site.register(Price, RichTextAdmin)
admin.site.register(Chegirmalar)
