from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'providers_by_zipcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search_by_zip/',include('search_by_zip.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
