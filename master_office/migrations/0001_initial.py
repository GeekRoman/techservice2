# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_service'),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField(verbose_name='Текст комментария')),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(default='', upload_to='')),
                ('phone', models.CharField(max_length=20, default='')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('begin_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
                ('expected_date', models.DateTimeField()),
                ('rating', models.IntegerField(default=0)),
                ('feedback', models.TextField()),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('brand_name', models.CharField(max_length=20)),
                ('device_name', models.CharField(max_length=20)),
                ('serial_id', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('trouble_description', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('master', models.ForeignKey(to='master_office.Master')),
                ('order', models.ForeignKey(to='master_office.Order')),
                ('service', models.ForeignKey(to='mainApp.Service')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='order',
            field=models.ForeignKey(to='master_office.Order'),
        ),
    ]
