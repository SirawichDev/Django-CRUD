from django.contrib import admin

# Register your models here.
from .models import Post
class IncreatOptionAdmin(admin.ModelAdmin):
    list_display = ["title","__unicode__","timestamp"]
    class Meta:
        model = Post

        
admin.site.register(Post,IncreatOptionAdmin)