from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register the BlogPost model with Summernote capabilities
@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    # Define how the BlogPost model is displayed in the admin interface
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register the Comment model
admin.site.register(Comment)
