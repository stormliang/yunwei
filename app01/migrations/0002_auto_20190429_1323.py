# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-04-29 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=32, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=32, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, verbose_name='书名'),
        ),
    ]
