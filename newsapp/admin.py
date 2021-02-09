from django.contrib import admin
from .models import Post, Category
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Post, MyModelAdmin)
admin.site.register(Category)
