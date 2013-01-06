#from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('map_site.FirstMap.views',
 # url(r'^$', 'index', name='FirstMap-index'),
    # Examples:
    # url(r'^$', 'map_site.views.home', name='home'),
    # url(r'^map_site/', include('map_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

# Import django modules
from django.conf.urls.defaults import *
from django.contrib import admin
# Import custom modules
import settings


admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('map_site.FirstMap.urls')),
)
