from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from userMgmt.models import UserContact
from newsletterMgmt.models import NewsLetterTemplate
from utils.mixins import BaseModel


#
class Campaign(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contacts = models.ManyToManyField(UserContact)
    newsletter_template = models.ForeignKey(NewsLetterTemplate, on_delete=models.CASCADE)
    dynamic_values = models.JSONField(default=dict)
    status = models.BooleanField(default=True)
    scheduled_time = models.DateTimeField(null=True)
    
    def schedule_emails(self):
        from .tasks import send_campaign_emails
        from django.utils import timezone

        # Calculate the time difference between now and the campaign time
        delta = self.scheduled_time - timezone.now()

        # Schedule the task to send emails
        send_campaign_emails.apply_async((self.pk,), countdown=delta.total_seconds())
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.schedule_emails()

    def __str__(self):
        return self.name

#
class CampaignSendStatus(models.Model):
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    recipient_user = models.ForeignKey(UserContact, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  # success, failed
    created_at = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.campaign.name} - {self.recipient_user.email} - {self.status}"


