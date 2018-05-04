from django.contrib import admin

# Register your models here.
from .models import Post
class IncreatOptionAdmin(admin.ModelAdmin):
    list_display = ["title","Comment","timestamp","updated"]
    list_display_links = ["updated","title"]
    list_filter = ["title","updated"]
    search_fields = ["title"]
    class Meta:
        model = Post

        
admin.site.register(Post,IncreatOptionAdmin)