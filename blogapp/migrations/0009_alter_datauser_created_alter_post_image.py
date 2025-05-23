# Generated by Django 5.1.6 on 2025-04-03 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_post_image_alter_datauser_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 3, 13, 21, 19, 591296)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
