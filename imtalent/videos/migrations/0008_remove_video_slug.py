# Generated by Django 3.0.4 on 2020-04-11 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20200410_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
    ]