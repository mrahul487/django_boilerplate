# Generated by Django 2.2.10 on 2020-04-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
