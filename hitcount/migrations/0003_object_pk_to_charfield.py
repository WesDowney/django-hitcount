# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitcount', '0002_index_ip_and_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitcount',
            name='object_pk',
            field=models.CharField(verbose_name='object ID', max_length=36, null=True, default=None),
        ),
    ]
