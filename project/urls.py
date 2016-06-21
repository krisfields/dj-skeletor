from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),  # NOQA
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<url>.*/)', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
