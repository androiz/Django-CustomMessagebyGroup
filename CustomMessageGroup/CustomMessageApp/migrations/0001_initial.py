# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b'', max_length=256)),
                ('role', models.ForeignKey(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.AddField(
            model_name='rolemessage',
            name='service',
            field=models.ForeignKey(to='CustomMessageApp.Services'),
        ),
    ]
