import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include ('blog.apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^plantilla/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

)

 # Examples:
    # url(r'^$', 'SistemaEncuesta.views.home', name='home'),
    # url(r'^SistemaEncuesta/', include('SistemaEncuesta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),