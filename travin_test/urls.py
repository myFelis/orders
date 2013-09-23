from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from order_system import views

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'travin_test.views.home', name='home'),
    # url(r'^travin_test/', include('travin_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if 'django.contrib.admin' in settings.INSTALLED_APPS and settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),
    )
