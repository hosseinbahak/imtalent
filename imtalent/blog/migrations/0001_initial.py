# Generated by Django 3.0.4 on 2020-03-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(null=True)),
                ('comments', models.IntegerField(null=True)),
                ('owner', models.ManyToManyField(blank=True, to='blog.Users')),
            ],
        ),
    ]
