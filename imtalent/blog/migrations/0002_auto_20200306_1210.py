# Generated by Django 3.0.4 on 2020-03-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='No Name', max_length=100),
        ),
        migrations.AddField(
            model_name='videos',
            name='name',
            field=models.CharField(default='No Name', max_length=100),
        ),
    ]