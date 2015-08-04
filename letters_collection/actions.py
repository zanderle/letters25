from django.core.mail import send_mail
from django.conf import settings


def notify_author(letter_submission):
    text = "Hey %s,\nthank you for submitting a letter to Letters to My 25-Year-Old Self! " % letter_submission.author + \
        "One of our editors will contact you with possible edits.\nBest,\nLetters to My 25-Year-Old Self"
    send_mail('Thank you for submitting a letter!', text, settings.DEFAULT_FROM, [letter_submission.email])


def notify_team(letter_submission):
    text = "Hi!\nThere is a new letter submission from %s. Visit the website to see the letter.\n" % letter_submission.author + \
        "Sincerely,\nYour friendly bot." 
    send_mail('New letter submission', text, settings.DEFAULT_FROM, settings.TEAM_EMAILS)
