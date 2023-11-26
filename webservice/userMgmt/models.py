from django.db import models
from django.contrib.auth.models import User

from utils.mixins import BaseModel
    

#
class UserContact(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email_id = models.EmailField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.email_id
    
