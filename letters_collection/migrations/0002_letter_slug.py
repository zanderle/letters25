# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='slug',
            field=models.SlugField(default=0, help_text=b'URL slug for this letter', unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
