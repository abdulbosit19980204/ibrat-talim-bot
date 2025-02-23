from django.contrib import admin
from api.models import BotUser, Feedback, Filial, FilialDetail, Yonalishlar, Fanlar, Price
from ckeditor.widgets import CKEditorWidget
from django.db import models


class RichTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget()},  # RichText qo‘shish
    }


admin.site.register(BotUser)
admin.site.register(Feedback)
admin.site.register(Filial)
admin.site.register(FilialDetail, RichTextAdmin)
admin.site.register(Yonalishlar)
admin.site.register(Fanlar)
admin.site.register(Price, RichTextAdmin)
