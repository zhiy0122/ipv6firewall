# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-05 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20191005_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='result',
            field=models.CharField(choices=[('true', '\u68c0\u6d4b\u6210\u529f'), ('false', '\u68c0\u6d4b\u5931\u8d25'), ('middle', '\u6b63\u5728\u68c0\u6d4b')], max_length=5, verbose_name='\u4efb\u52a1\u72b6\u6001'),
        ),
    ]
