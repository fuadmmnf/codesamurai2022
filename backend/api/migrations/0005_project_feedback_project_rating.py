# Generated by Django 4.1.4 on 2022-12-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_latitute_project_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='feedback',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='project',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]