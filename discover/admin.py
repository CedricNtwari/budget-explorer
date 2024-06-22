from django.contrib import admin
from .models import Post, Comment, Favorite
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'author', 'budget', 'currency', 'location', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'author', 'currency')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')


admin.site.register(Comment)
admin.site.register(Favorite)
