from django.contrib import admin
from .models import Blog, BlogTitle
# Register your models here.

@admin.register(Blog)
class BlogAdmin (admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ["title"],
    }
    search_fields = ('title',)
    list_filter = ['date']
    exclude = ('view',)



admin.site.register(BlogTitle)
