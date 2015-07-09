# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(help_text=b'Author of the letter', max_length=255)),
                ('occupation', models.CharField(help_text=b"Author's occupation", max_length=100)),
                ('age', models.CharField(help_text=b"Author's age", max_length=10)),
                ('location', models.CharField(help_text=b"Author's location", max_length=100)),
                ('letter', models.TextField(help_text=b'The letter itself')),
                ('published', models.BooleanField(default=False, help_text=b'Should this letter be published?')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
                ('timestamp_published', models.DateTimeField(help_text=b'When was this letter published', null=True, blank=True)),
                ('illustration', filer.fields.image.FilerImageField(related_name='letter_illustration', blank=True, to='filer.Image', help_text=b'Illustration for this letter', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LetterSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(help_text=b'Your first and last name', max_length=255)),
                ('email', models.EmailField(help_text=b'Your email', max_length=254)),
                ('occupation', models.CharField(help_text=b'Your occupation', max_length=100)),
                ('age', models.CharField(help_text=b'Your age', max_length=10)),
                ('location', models.CharField(help_text=b'Your location', max_length=100)),
                ('letter', models.TextField(help_text=b'The letter itself')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='letter',
            name='submission',
            field=models.ForeignKey(related_name='letter_object', blank=True, to='letters_collection.LetterSubmission', help_text=b'Submission for this letter', null=True),
        ),
    ]
