# Generated by Django 4.2.4 on 2023-09-25 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_foto_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
