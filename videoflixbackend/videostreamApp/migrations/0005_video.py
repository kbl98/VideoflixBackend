# Generated by Django 4.2.2 on 2023-06-19 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostreamApp', '0004_remove_myuser_date_of_birth_myuser_verification_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='videos')),
            ],
        ),
    ]
