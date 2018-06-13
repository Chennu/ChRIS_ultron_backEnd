# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-04-30 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0018_auto_20180423_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='execshell',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plugin',
            name='selfexec',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plugin',
            name='selfpath',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plugin',
            name='authors',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='license',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='title',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='version',
            field=models.CharField(max_length=10),
        ),
    ]