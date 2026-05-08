from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'published_date', 'created_at', 'updated_at')
    list_filter = ('published_date', 'created_at', 'updated_at')
    search_fields = ('post_title', 'post_content')
    ordering = ('-published_date',)

admin.site.register(Post, PostAdmin)
