from django.contrib import admin
from .models import English_Unit, English_Chapter
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(English_Unit, MyModelAdmin)
admin.site.register(English_Chapter)
