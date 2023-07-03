from django.db import models
from django.contrib.auth.models import User
from authemail.models import EmailUserManager, EmailAbstractUser
from datetime  import date
from import_export import resources
from datetime import datetime
import json
from django.conf import settings
import os
from import_export import resources
from import_export.fields import Field
from import_export.widgets import JSONWidget
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import tablib



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
    file_480 = models.FileField(default='',upload_to='videos', blank=True, null=True)
    file_720 = models.FileField(default='',upload_to='videos', blank=True, null=True)
    file_1000 = models.FileField(default='',upload_to='videos', blank=True, null=True)
    

    
        


    def __str__(self):
        return self.title
    

class VideoResource(resources.ModelResource):
    class Meta:
        model = Video
        fields = ('title', 'description', 'created_at','file')  # Füge hier die gewünschten Felder hinzu
        export_order = fields

    def __str__(self):
        return self.title

    

def export_videos():
    dataset = VideoResource().export()
    dataset_json = dataset.json
    print(dataset_json)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(settings.BACKUP_ROOT, f"videos_{timestamp}.json")
    print(backup_path)

    os.makedirs(settings.BACKUP_ROOT, exist_ok=True)

    with open(backup_path, 'w') as file:
        file.write(dataset_json)

if __name__ == "__main__":
    export_videos()


def import_videos(backup):
    video_resource = resources.modelresource_factory(model=Video)()

    with open(backup, 'r') as file:
        json_data = json.load(file)

    for video_json in json_data:
        dataset = dataset.Dataset()
        dataset.json = video_json
        result = video_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
           
            result = video_resource.import_data(dataset, dry_run=False)
            if result.has_errors():
                # Behandeln von Fehlern beim Import
                print(result.errors)
            else:
               
                print(f"Das Video  wurde erfolgreich importiert.")
        else:
            # Fehler beim Probeimport des aktuellen Videos
            print(result.errors)




