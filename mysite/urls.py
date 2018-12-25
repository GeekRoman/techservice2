from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^', include('mainApp.urls')),
    url(r'^webexample/', include("webexample.urls")),
    url(r'^news/', include("news.urls")),
    url(r'^master/', include("master_office.urls")),
    url(r'^client/', include("client_office.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)