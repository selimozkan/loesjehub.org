# Generated by Django 5.1.5 on 2025-01-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pageheader_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageheader',
            name='page',
            field=models.CharField(choices=[('about', 'ABOUT THE PROJECT'), ('partners', 'PARTNERS'), ('projects', 'PROJECTS'), ('resources', 'RESOURCES'), ('contact', 'CONTACT')], default='about', max_length=25, verbose_name='Related Page'),
        ),
    ]
