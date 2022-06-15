# Generated by Django 4.0.4 on 2022-06-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_user_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.profile'),
            preserve_default=False,
        ),
    ]
