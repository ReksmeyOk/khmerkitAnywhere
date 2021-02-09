
from django.contrib import admin
from .models import PTHN_Unit, PTHN_Chapter
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(PTHN_Unit, MyModelAdmin)
admin.site.register(PTHN_Chapter)
