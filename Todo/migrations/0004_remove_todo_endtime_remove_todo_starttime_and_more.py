# Generated by Django 4.1 on 2022-08-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_todo_endtime_todo_starttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='startTime',
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
