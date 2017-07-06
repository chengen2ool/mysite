# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-06 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, unique=True)),
                ('status', models.IntegerField(default=1)),
                ('remark', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=50)),
                ('min', models.IntegerField(default=0)),
                ('max', models.IntegerField(default=0)),
                ('is_null', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='caseconf',
            name='interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automated_testing.InterfaceConf'),
        ),
    ]