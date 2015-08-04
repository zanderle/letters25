from django.db import models
from filer.fields.image import FilerImageField
from markupfield.fields import MarkupField
from django.utils import timezone


class Letter(models.Model):
    author = models.CharField(max_length=255, help_text='Author of the letter')
    slug = models.SlugField(max_length=100, unique=True, help_text='URL slug for this letter')
    occupation = models.CharField(max_length=100, help_text="Author's occupation")
    age = models.IntegerField(help_text="Author's age")
    location = models.CharField(max_length=100, help_text="Author's location")
    illustration = FilerImageField(
        null=True,
        blank=True,
        help_text='Illustration for this letter',
        related_name="letter_illustration"
        )
    letter = MarkupField(default_markup_type='markdown', help_text='The letter itself')
    letter_length = models.IntegerField(
        blank=True,
        help_text='What is the approximate reading length of this letter. Leave empty for autofill.'
        )
    published = models.BooleanField(default=False, help_text='Should this letter be published?')
    popularity_index = models.IntegerField(
        blank=True,
        default=0,
        help_text='The letter with higher index, will be shown as more popular. \
        (This is only a temporary measure, until I automate it)'
        )
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_edited = models.DateTimeField(auto_now=True)
    timestamp_published = models.DateTimeField(
        blank=True,
        default=timezone.now,
        help_text='When was this letter published (leave empty for auto-fill)'
        )
    submission = models.ForeignKey(
        'letters_collection.LetterSubmission',
        null=True,
        blank=True,
        help_text='Submission for this letter',
        related_name='letter_object'
        )

    class Meta:
        ordering = ['-timestamp_created']

    def __unicode__(self):
        return self.author

    def save(self, *args, **kwargs):
        # Fill in self.letter_length if it is empty
        if not self.letter_length:
            self.letter_length = self.get_reading_length
        super(Letter, self).save(*args, **kwargs)

    def get_reading_length(self):
        """
        Return estimated reading length of this letter rounded up to the minute.
        """
        number_of_char = len(self.letter.raw)
        estimate = number_of_char / 1000  # Estimated reading length in minutes
        estimate = round(estimate)
        return estimate
        # return '%s min' % estimate if estimate else '< 1 min'


class LetterSubmission(models.Model):
    author = models.CharField(max_length=255, help_text='Your first and last name')
    email = models.EmailField(help_text='Your email')
    occupation = models.CharField(max_length=100, help_text="Your occupation")
    age = models.IntegerField(help_text="Your age")
    location = models.CharField(max_length=100, help_text="Your location")
    letter = models.TextField(help_text='The letter itself')
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp_created']

    def __unicode__(self):
        return self.author
