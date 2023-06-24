import os
import subprocess

def convert_480(source):
    print(source)
    source_name=os.path.splitext(source)[0]
    print(source_name)
    new_file=source_name + '_480.mp4'
    ##cmd = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(source, new_file)
    cmd = ['ffmpeg', '-i', source, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', new_file]
    subprocess.run(cmd)