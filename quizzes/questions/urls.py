from django.conf.urls import url

from . import views

app_name = 'questions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^all/$', views.all, name='all'),
]
