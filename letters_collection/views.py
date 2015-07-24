from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Letter
from .forms import SubmissionForm


class IndexView(ListView):
    model = Letter
    template_name = 'index.html'
    queryset = Letter.objects.filter(published=True).order_by('-timestamp_published', '-timestamp_created')
    letters_list = 'latest'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        featured = Letter.objects.filter(published=True).latest('timestamp_published')
        submitted = self.request.GET.get('submitted')
        context.update({'featured': featured, 'submitted': submitted})
        return context

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        if self.letters_list == 'latest':
            return qs
        elif self.letters_list == 'popular':
            return qs.order_by('-popularity_index', '-timestamp_published', '-timestamp_created')


class CategoryView(ListView):
    model = Letter
    template_name = 'category_detail.html'

    # def get_queryset(self):


class LetterView(DetailView):
    model = Letter
    template_name = 'letter_detail.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class SubmitView(FormView):
    form_class = SubmissionForm
    template_name = 'submit.html'
    success_url = '/?submitted=1'
