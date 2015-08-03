# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=256, verbose_name='\u57df\u540d')),
                ('state', models.CharField(max_length=20, verbose_name='\u72b6\u6001', choices=[(b'unknown', '\u672a\u77e5'), (b'used', '\u5728\u4f7f\u7528'), (b'free', '\u672a\u4f7f\u7528')])),
            ],
        ),
    ]
