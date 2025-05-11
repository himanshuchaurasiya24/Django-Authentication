from django.contrib import admin

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'is_draft', 'category')

admin.site.register(Blog, BlogAdmin)

