from django.contrib import admin
from .models import AI_Unit, AI_Chapter
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(AI_Unit, MyModelAdmin)
admin.site.register(AI_Chapter)
