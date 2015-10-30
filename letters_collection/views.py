from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from .models import Letter
from .forms import SubmissionForm
from .actions import notify_author, notify_team


class IndexView(ListView):
    model = Letter
    template_name = 'index.html'
    letters_list = 'latest'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # For admins show the latest letter
        # For normal users show the latest published letter
        featured = Letter.objects.all() if self.request.user.is_superuser else Letter.objects.filter(published=True)
        featured = featured.latest('timestamp_published')

        if self.letters_list == 'popular':
            featured = Letter.objects.filter(published=True).order_by(
                '-popularity_index',
                '-timestamp_published',
                '-timestamp_created'
                )[0]
        submitted = self.request.GET.get('submitted')
        context.update({'featured': featured, 'submitted': submitted})
        return context

    def get_queryset(self):
        # For admins show all the letters but for normal users show only published letters
        qs = Letter.objects.all() if self.request.user.is_superuser else Letter.objects.filter(published=True)
        if self.letters_list == 'latest':
            return qs.order_by('-timestamp_published', '-timestamp_created')
        elif self.letters_list == 'popular':
            return qs.order_by('-popularity_index', '-timestamp_published', '-timestamp_created')[:15]


class CategoriesView(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        selected = self.request.GET.get('category', 'age')
        context.update({
            'selected': selected,
            'five_min_letters': Letter.objects.filter(letter_length__lt=5).count(),
            'ten_min_letters': Letter.objects.filter(letter_length__lt=10, letter_length__gte=5).count(),
            'fifteen_min_letters': Letter.objects.filter(letter_length__gte=10).count()
        })
        return context


class CategoryView(ListView):
    model = Letter
    template_name = 'category_detail.html'
    interval = []
    selected = ''

    def get_queryset(self):
        category = self.kwargs.get('category')
        interval = self.kwargs.get('interval')
        self.selected = category
        try:
            interval = interval.split('-')
            if len(interval) > 2 or len(interval) < 1:
                raise Http404
            self.interval = interval
            interval = [int(i) for i in interval]
        except:
            raise Http404
        if category == 'age':
            letters = Letter.objects.filter(published=True).filter(age__gte=interval[0])
            if len(interval) == 2:
                letters = letters.filter(age__lte=interval[1])
            return letters.order_by('age', '-timestamp_published')
        elif category == 'length':
            letters = Letter.objects.filter(published=True).filter(letter_length__gte=interval[0])
            if len(interval) == 2:
                letters = letters.filter(letter_length__lt=interval[1])
            return letters.order_by('letter_length', '-timestamp_published')
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        if self.selected == 'length':
            value = " - ".join(self.interval) + ' min'
        else:
            value = " - ".join(self.interval)
        context.update({'value': value, 'selected': self.selected})
        return context


class LetterView(DetailView):
    model = Letter
    template_name = 'letter_detail.html'

    def get_queryset(self):
        # For admins show all the letters but for normal users show only published letters
        qs = Letter.objects.all() if self.request.user.is_superuser else Letter.objects.filter(published=True)
        return qs.order_by('-timestamp_published', '-timestamp_created')

    def get_context_data(self, **kwargs):
        context = super(LetterView, self).get_context_data(**kwargs)
        try:
            next_letter = self.object.get_next_by_timestamp_published(published=True)
        except Exception:
            next_letter = Letter.objects.filter(published=True).earliest('timestamp_published')
        try:
            previous_letter = self.object.get_previous_by_timestamp_published(published=True)
        except Exception:
            previous_letter = Letter.objects.filter(published=True).latest('timestamp_published')
        context.update({
            'next_letter': next_letter,
            'previous_letter': previous_letter
        })
        return context


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class SubmitView(FormView):
    form_class = SubmissionForm
    template_name = 'submit.html'
    success_url = '/?submitted=1'

    def form_valid(self, form):
        if not form.cleaned_data['phonenumber']:  # Check the honeypot
            # Save the Submission
            obj = form.save()
            # Send an email to author
            notify_author(obj)
            # Notify the letters team
            notify_team(obj)
        else:
            print "Gotcha!"
        return super(SubmitView, self).form_valid(form)
