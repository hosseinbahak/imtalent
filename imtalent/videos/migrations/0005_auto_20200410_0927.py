# Generated by Django 3.0.4 on 2020-04-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20200409_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank='False', default='default.png', max_length=10000000, upload_to='media/video_files/'),
        ),
    ]