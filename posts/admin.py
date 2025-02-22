from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'updated')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-date_posted',)

admin.site.register(Post, PostAdmin)
