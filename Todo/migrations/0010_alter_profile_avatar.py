# Generated by Django 4.1 on 2022-10-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0009_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/profile2.png', null=True, upload_to=''),
        ),
    ]
