# Generated by Django 2.2.1 on 2019-06-24 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userinfo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
