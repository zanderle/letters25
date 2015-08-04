from django.core.mail import send_mail
from django.conf import settings


def notify_author(letter_submission):
    text = "Hello %s!\n\nThank you for submitting a letter to your 25-year-old self." % letter_submission.author + \
        "We know it took something for you to write that letter.\n\n" + \
        "We look forward to reading it and we'll be reaching out to you soon with our edits and feedback.\n\n" + \
        "Thank you for your patience.\n\n" + \
        "Very best,\nThe team at Letters to My 25-Year-Old Self"
    send_mail('Thank you for submitting a letter!', text, settings.DEFAULT_FROM, [letter_submission.email])


def notify_team(letter_submission):
    text = "Hi!\n\nThere is a new letter submission from %s. Visit the website to see the letter.\n\n" % letter_submission.author + \
        "Sincerely,\nYour friendly bot."
    send_mail('New letter submission', text, settings.DEFAULT_FROM, settings.TEAM_EMAILS)
