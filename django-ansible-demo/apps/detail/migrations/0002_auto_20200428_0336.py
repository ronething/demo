# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticsrecord',
            name='datatime',
            field=models.DateTimeField(default=b'2020-04-28', verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
