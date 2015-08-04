from django.contrib import admin
from . import models

class LetterAdmin(admin.ModelAdmin):
    pass

class LetterSubmissionAdmin(admin.ModelAdmin):
    pass
    # TODO Create action 'create letter from submission'

admin.site.register(models.Letter, LetterAdmin)
admin.site.register(models.LetterSubmission, LetterSubmissionAdmin)
