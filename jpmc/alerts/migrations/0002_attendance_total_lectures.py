# Generated by Django 2.2.8 on 2020-08-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='total_lectures',
            field=models.IntegerField(default=0),
        ),
    ]
