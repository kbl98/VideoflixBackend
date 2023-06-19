from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video
import os

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_save,sender=Video)
def send_post_save(sender,instance,created,**kwargs):
    print('Video save')
    if created:
        print('New Video saved')

@receiver(post_delete,sender=Video)
def send_post_delete(sender,instance,**kwargs):
    print('Video deleted')
    if instance.file:
        _delete_file(instance.file.path)



