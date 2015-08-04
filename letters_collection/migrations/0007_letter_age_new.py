# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0006_auto_20150729_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='age_new',
            field=models.IntegerField(default=0, help_text=b"Author's age"),
            preserve_default=False,
        ),
    ]
