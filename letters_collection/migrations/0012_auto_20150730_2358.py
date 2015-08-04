# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def get_reading_length(letter):
    """
    Return estimated reading length of this letter rounded up to the minute.
    """
    number_of_char = len(letter.letter.raw)
    estimate = number_of_char / 800  # Estimated reading length in minutes
    estimate = round(estimate)
    return estimate


def calculate_reading_length(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Letter = apps.get_model("letters_collection", "Letter")
    for letter in Letter.objects.all():
        letter.letter_length = get_reading_length(letter)
        letter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0011_letter_letter_length'),
    ]

    operations = [
        migrations.RunPython(calculate_reading_length),
    ]
