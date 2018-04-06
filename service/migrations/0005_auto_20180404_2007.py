# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_categoryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=service.models.UploadImageForService, verbose_name='Изображение'),
        ),
    ]