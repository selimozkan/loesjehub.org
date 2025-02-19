# Generated by Django 5.1.5 on 2025-01-22 11:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_about_specificobjective'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='objectives_image',
            field=models.ImageField(blank=True, null=True, upload_to='home/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='homepage',
            name='objectives_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
