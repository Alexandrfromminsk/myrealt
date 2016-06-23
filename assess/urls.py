from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^full/$', views.full_index, name='full_index'),
    url(r'^(?P<rating_id>[0-9]+)/$', views.detail, name='detail'),
]