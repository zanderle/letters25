# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0009_remove_letter_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='age_new',
            new_name='age',
        ),
    ]
