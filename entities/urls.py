from django.conf.urls import patterns, url

from entities.views import EntityListView

urlpatterns = patterns('',
    url(r'^$, EntityListView.as_view()', name='entities-list'),
)
