from django.contrib import admin
from .models import Campaign, CampaignSendStatus


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'modified_at')
    search_fields = ('name', )


class CampaignSendStatusAdmin(admin.ModelAdmin):
    list_display = ('campaign_id', 'recipient_user', 'status', 'created_at')
    search_fields = ('campaign_id', )
    

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CampaignSendStatus, CampaignSendStatusAdmin)