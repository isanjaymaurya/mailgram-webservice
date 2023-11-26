from django.contrib import admin
from .models import NewsLetterTemplate


class NewsletterTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'modified_at')
    search_fields = ('name', 'status', 'created_at', 'modified_at')


admin.site.register(NewsLetterTemplate, NewsletterTemplateAdmin)
