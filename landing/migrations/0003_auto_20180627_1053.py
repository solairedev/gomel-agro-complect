# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20180626_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textblock',
            name='content',
            field=models.TextField(blank=True, help_text='Если в блоке нужен простой текст, используйте это поле', null=True, verbose_name='Контент блока'),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='extend_content',
            field=models.TextField(blank=True, null=True, verbose_name='Расширенный редактор блока'),
        ),
    ]
