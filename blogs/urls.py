from django.conf.urls import url

from . import views

app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<content_id>[0-9]+)/$', views.detail, name='detail'),
]


