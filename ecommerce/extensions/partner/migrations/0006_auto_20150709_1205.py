# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_auto_20150610_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='users',
            field=models.ManyToManyField(related_name='partners', verbose_name='Users', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
