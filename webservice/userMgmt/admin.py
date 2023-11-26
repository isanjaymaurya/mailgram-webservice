from django.contrib import admin
from .models import UserContact


class UserContactAdmin(admin.ModelAdmin):
    list_display = ('email_id', 'status', 'created_at', 'modified_at')
    search_fields = ('email_id', )


admin.site.register(UserContact, UserContactAdmin)