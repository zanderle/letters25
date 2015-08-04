# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def convert_age(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Letter = apps.get_model("letters_collection", "Letter")
    for letter in Letter.objects.all():
        letter.age_new = int(letter.age)
        letter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0007_letter_age_new'),
    ]

    operations = [
        migrations.RunPython(convert_age),
    ]
