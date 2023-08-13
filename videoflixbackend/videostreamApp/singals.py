from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video
import os
from .tasks import convert_480,convert_720
from .tasks import convert_1000
import django_rq
from videostreamApp.models import export_videos

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)
   

    
    

@receiver(post_save,sender=Video)
def send_post_save(sender,instance,created,**kwargs):
    print('Video save')
    if created:
        print('New Video saved')
        queue = django_rq.get_queue('default',autocommit=True)
        queue.enqueue(convert_480,instance.file.path)
        queue.enqueue(convert_720,instance.file.path)
        queue.enqueue(convert_1000,instance.file.path)
        


@receiver(post_delete,sender=Video)
def send_post_delete(sender,instance,**kwargs):
    print('Video deleted')
    if instance.file:
      _delete_file(instance.file.path)
      _delete_file(instance.file_480.path)
      _delete_file(instance.file_720.path)
      _delete_file(instance.file_1000.path)

   

    

@receiver(post_save,sender=Video)
def export_videos_post_save(sender, instance, **kwargs):
    export_videos()


