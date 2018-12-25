# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180327_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('time', models.CharField(max_length=20, help_text='How much time service will take')),
                ('price', models.IntegerField()),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.Area')),
            ],
        ),
    ]
