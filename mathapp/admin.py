from django.contrib import admin
from .models import Math_Unit, Math_Chapter
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Math_Unit, MyModelAdmin)
admin.site.register(Math_Chapter)
