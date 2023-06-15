from django.db import models
from django.contrib.auth.models import User
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Custom fields
    objects = EmailUserManager()
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
   
    # We inherit the other fields and methods from the AbstractUser model
    
    def __str__(self):
        return self.email

	# Required
	


# Create your models here.

