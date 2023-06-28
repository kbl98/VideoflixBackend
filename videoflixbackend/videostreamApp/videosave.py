from .models import VideoResource
from datetime import datetime
import json
from django.conf import settings
import os


#def export_videos():
   # dataset = VideoResource().export()
   # print('111111111111111111111111111111'+repr(dataset))
    #dataset=json.dumps(dataset)
   
    #timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #backup_path = os.path.join(settings.BACKUP_ROOT, f"videos_{timestamp}.json")
    

    #os.makedirs(settings.BACKUP_ROOT, exist_ok=True)
   # with open(backup_path, 'w') as file:
    #    file.write(dataset)

#if __name__ == "__main__":
#    export_videos()