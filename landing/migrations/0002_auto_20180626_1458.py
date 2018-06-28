# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageitem',
            name='custom_style',
            field=models.CharField(blank=True, help_text='В этом поле вы можете задать css для изображения', max_length=300, null=True, verbose_name='Стили'),
        ),
        migrations.AlterField(
            model_name='imageitem',
            name='identifier',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Идентификатор группы'),
        ),
    ]
