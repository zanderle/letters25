from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^popular/$', views.IndexView.as_view(letters_list='popular'), name='popular'),
    url(r'^categories/$', views.IndexView.as_view(letters_list='categories'), name='categories'),
    url(r'^letters/(?P<slug>[\w-]+)/$', views.LetterView.as_view(), name='letter'),
    url(r'^project/$', views.AboutUsView.as_view(), name='project'),
    url(r'^submit/$', views.SubmitView.as_view(), name='submit'),
]
