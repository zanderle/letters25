from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Letter
from .forms import SubmissionForm


class IndexView(ListView):
    model = Letter
    template_name = 'index.html'
    queryset = Letter.objects.filter(published=True)


class LetterView(DetailView):
    model = Letter


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class SubmitView(FormView):
    form_class = SubmissionForm
    template_name = 'submit.html'
