# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thresher', '0016_answer_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='order',
        ),
        migrations.AddField(
            model_name='article',
            name='batch_name',
            field=models.TextField(db_index=True, default=b''),
        ),
        migrations.AddField(
            model_name='topic',
            name='namespace',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_number',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]