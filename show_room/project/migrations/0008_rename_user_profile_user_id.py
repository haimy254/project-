# Generated by Django 4.0.4 on 2022-06-15 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_remove_project_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
    ]