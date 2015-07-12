from django.contrib import admin
from . import models

class LetterAdmin(admin.ModelAdmin):
    pass

class LetterSubmissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Letter, LetterAdmin)
admin.site.register(models.LetterSubmission, LetterSubmissionAdmin)
