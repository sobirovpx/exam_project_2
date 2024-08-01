from django.contrib import admin

from blogs.models import Blog, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'auther_id', 'content', 'image']



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'education')

