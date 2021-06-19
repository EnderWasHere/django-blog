from django.contrib import admin

# Register your models here.

from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title","slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}