# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv', '0002_item_lastname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Tenant',
        ),
    ]
