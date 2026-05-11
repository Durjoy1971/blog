from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'published_date', 'created_at', 'updated_at')
    list_filter = ('published_date', 'created_at', 'updated_at')
    search_fields = ('post_title', 'post_content')
    ordering = ('published_date',)
    list_display_links = ('id', 'post_title')

# admin.site.register(Post, PostAdmin)
admin.site.site_header = "My Blog Administration"
admin.site.site_title = "My Blog Admin"
admin.site.index_title = "Welcome to My Blog Management"