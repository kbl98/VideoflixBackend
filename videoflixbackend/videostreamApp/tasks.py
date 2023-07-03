import os
import subprocess
from .models import Video

def convert_480(source):
    print(source)
    source_name=os.path.splitext(source)[0]
    print(source_name)
    new_file=source_name + '_480.mp4'
    ##cmd = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(source, new_file)
    cmd = ['ffmpeg', '-i', source, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', new_file]
    process = subprocess.Popen(cmd)
    process.wait()
    filename = os.path.basename(source)
    video = Video.objects.get(file__icontains=filename)
    video.file_480.save(os.path.basename(new_file), open(new_file, 'rb'), save=True)
    os.remove(new_file)

def convert_720(source):
    print(source)
    source_name=os.path.splitext(source)[0]
    print(source_name)
    new_file=source_name + '_720.mp4'
    ##cmd = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(source, new_file)
    cmd = ['ffmpeg', '-i', source, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', new_file]
    process = subprocess.Popen(cmd)
    process.wait()
    filename = os.path.basename(source)
    video = Video.objects.get(file__icontains=filename)
    video.file_720.save(os.path.basename(new_file), open(new_file, 'rb'), save=True)
    os.remove(new_file)

def convert_1000(source):
    print(source)
    source_name=os.path.splitext(source)[0]
    print(source_name)
    new_file=source_name + '_1000.mp4'
    ##cmd = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(source, new_file)
    cmd = ['ffmpeg', '-i', source, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', new_file]
    process = subprocess.Popen(cmd)
    process.wait()
    filename = os.path.basename(source)
    video = Video.objects.get(file__icontains=filename)
    video.file_1000.save(os.path.basename(new_file), open(new_file, 'rb'), save=True)
    os.remove(new_file)
  

