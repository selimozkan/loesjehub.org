# Generated by Django 5.1.5 on 2025-01-21 21:00

import django.core.validators
import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_pageheader_page'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_image', models.ImageField(upload_to='home/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])])),
                ('welcome_title', models.CharField(blank=True, max_length=75, null=True)),
                ('welcome_description', models.TextField(blank=True, null=True)),
                ('latest_projects_title', models.CharField(blank=True, max_length=75, null=True)),
                ('latest_projects_description', models.TextField(blank=True, null=True)),
                ('impressum', models.TextField(blank=True, null=True)),
                ('privacy_policy', models.TextField(blank=True, null=True)),
                ('disclaimer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home Items',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Objective',
                'verbose_name_plural': 'Objectives',
                'ordering': ('id',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])])),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('linktree', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('id',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])])),
                ('partners', multiselectfield.db.fields.MultiSelectField(choices=[('berlin', 'Loesje Berlin'), ('bulgaria', 'Loesje Bulgaria'), ('bitola', 'Loesje Bitola'), ('gnu', 'GNU')], max_length=26)),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('ongoing', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('author__username', '-updated_at'),
                'managed': True,
            },
        ),
    ]
