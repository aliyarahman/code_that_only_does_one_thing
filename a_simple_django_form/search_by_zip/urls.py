from django.conf.urls import patterns, include, url
from search_by_zip import views

urlpatterns = patterns('',
	url(r'^index/$', views.index, name='index'),
	url(r'^results/(?P<zipentered>\d+)/$', views.results, name='results'), # for now these are simple
)