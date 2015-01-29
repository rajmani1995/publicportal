# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0002_auto_20150129_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='userid',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
