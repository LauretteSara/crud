# Generated by Django 4.1.4 on 2022-12-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateurs',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
