from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [

    #Admin Sites
    url(r'^admin/', include(admin.site.urls), name='admin'),
   

    #Sites
    url(r'^', include('website.urls')),
    url(r'^up/', include('devup.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)