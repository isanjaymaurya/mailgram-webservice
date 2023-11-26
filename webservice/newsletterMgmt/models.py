from django.db import models
from utils.mixins import BaseModel

#
class NewsLetterTemplate(BaseModel):
    name = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name