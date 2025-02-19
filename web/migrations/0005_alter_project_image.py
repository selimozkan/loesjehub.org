# Generated by Django 5.1.5 on 2025-01-21 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_homepage_objective_partner_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])]),
        ),
    ]
