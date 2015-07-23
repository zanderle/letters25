# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0003_auto_20150712_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='_letter_rendered',
            field=models.TextField(default='.', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='letter_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')]),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter',
            field=markupfield.fields.MarkupField(help_text=b'The letter itself', rendered_field=True),
        ),
    ]
