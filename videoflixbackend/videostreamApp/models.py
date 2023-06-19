from django.db import models
from django.contrib.auth.models import User
from authemail.models import EmailUserManager, EmailAbstractUser
from datetime  import date

class MyUser(EmailAbstractUser):
	# Custom fields
    objects = EmailUserManager()
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
   
    # We inherit the other fields and methods from the AbstractUser model
    
    def __str__(self):
        return self.email

	# Required
	
class Video(models.Model):
    created_at=models.DateField(default=date.today)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    file= models.FileField(upload_to ='videos',blank=True, null=True)

    def __str__(self):
        return self.title

# Create your models here.

