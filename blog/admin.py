from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'is_image')
    list_filter = ('title',)
    # search_fields = ('name', 'description',)
