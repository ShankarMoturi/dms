# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FID', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('user_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.IntegerField(default=0)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='filesystem',
            name='users',
            field=models.ForeignKey(to='data_app.Registration'),
        ),
    ]
