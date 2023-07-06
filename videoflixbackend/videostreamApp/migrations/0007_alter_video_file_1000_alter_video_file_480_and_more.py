# Generated by Django 4.2.2 on 2023-07-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostreamApp', '0006_video_file_1000_video_file_480_video_file_720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file_1000',
            field=models.FileField(blank=True, default='', null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file_480',
            field=models.FileField(blank=True, default='', null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file_720',
            field=models.FileField(blank=True, default='', null=True, upload_to='videos'),
        ),
    ]