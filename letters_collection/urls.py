from django.conf.urls import url
from django.views.generic import TemplateView
from .views import IndexView, CategoryView, LetterView, AboutUsView, SubmitView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^popular/$', IndexView.as_view(letters_list='popular'), name='popular'),
    url(r'^categories/$', TemplateView.as_view(template_name='categories.html'), name='categories'),
    url(r'^categories/(?P<category>[\w-]+)/$', CategoryView.as_view(), name='category_detail'),
    url(r'^letters/(?P<slug>[\w-]+)/$', LetterView.as_view(), name='letter'),
    url(r'^project/$', AboutUsView.as_view(), name='project'),
    url(r'^submit/$', SubmitView.as_view(), name='submit'),
]
