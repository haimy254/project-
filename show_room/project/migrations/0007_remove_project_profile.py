# Generated by Django 4.0.4 on 2022-06-15 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_profile_user_alter_project_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
    ]
