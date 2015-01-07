from django.conf.urls import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include(site.urls)),  # NOQA
    (r'^grappelli/', include('grappelli.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),  # NOQA
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}))
