from django.forms import ModelForm
from .models import LetterSubmission


def SubmissionForm(ModelForm):
    class Meta:
        model = LetterSubmission
        fields = ['author', 'age', 'occupation', 'location', 'letter']
