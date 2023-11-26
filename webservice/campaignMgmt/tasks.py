import logging
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail

from .models import Campaign, CampaignSendStatus
from userMgmt.models import UserContact
from newsletterMgmt.models import NewsLetterTemplate


logger = logging.getLogger(__name__)

# your_app/tasks.py

def render_email_content(newsletter_template, contact, dynamic_values):
    """
    Customize email content based on the newsletter template, contact, and dynamic values.
    """
    # Access the HTML content from the newsletter template
    template_content = newsletter_template.content

    # Replace dynamic values in the template content
    for key, value in dynamic_values.items():
        placeholder = f"{{{{ {key} }}}}"
        template_content = template_content.replace(placeholder, str(value))

    # You can also customize the content based on the contact information if needed
    # For example, you might want to personalize the email with the contact's name

    # In a real-world scenario, you might use a template engine like Jinja to render the content

    return template_content

#
@shared_task
def send_campaign_emails(campaign_id):
    try:
        campaign = Campaign.objects.get(pk=campaign_id)
        
        if campaign.scheduled_time <= timezone.now():
            # get contacts associated with campaign
            contacts = campaign.contacts.all()
            
            for contact in contacts:
                try:
                    recipient_user = contact.email_id
                    
                    newsletter_template = campaign.newsletter_template
                    
                    dynamic_values = campaign.dynamic_values
                    
                    email_content = render_email_content(newsletter_template, contact, dynamic_values)
                    
                    send_mail(
                        subject=newsletter_template.subject,
                        html_message=email_content,
                        from_email='its.sanjaymaurya@gmail.com',
                        recipient_list=[recipient_user],
                        fail_silently=False
                    )
                    
                    CampaignSendStatus.objects.create(
                        campaign=campaign,
                        recipient_user=recipient_user,
                        status='success'
                    )
                    
                    logger.info(f"Email sent successfully for campaign {campaign.name}")

                except Exception as e:
                    CampaignSendStatus.objects.create(
                        campaign=campaign,
                        recipient_email=contact.email_id,
                        status='Success',
                        error=str(e)
                    )
                    logger.error(f"Failed to campaign: {campaign.name}. Error: {str(e)}")

    except Exception as e:
        logger.error(e)