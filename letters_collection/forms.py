from django.forms import ModelForm, Textarea
from .models import LetterSubmission


class SubmissionForm(ModelForm):
    class Meta:
        model = LetterSubmission
        fields = ['author', 'age', 'occupation', 'location', 'letter']
        widgets = {
            'letter': Textarea(attrs={'rows': 4})
        }

    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-submit'})

# TODO On save send notification to the author and to our team
