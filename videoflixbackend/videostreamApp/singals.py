from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video
import os
from .tasks import convert_480
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
        convert_480(instance.file.path)


@receiver(post_delete,sender=Video)
def send_post_delete(sender,instance,**kwargs):
    print('Video deleted')
    if instance.file:
        _delete_file(instance.file.path)
    source_name = os.path.splitext(instance.file.path)[0]
    converted_file_path = source_name + '_480.mp4'
    _delete_file(converted_file_path)


    

@receiver(post_save,sender=Video)
def export_videos_post_save(sender, instance, **kwargs):
    export_videos()


