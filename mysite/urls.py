from django.contrib.sitemaps.views import sitemap
from core.sitemaps import ApplicationSitemap
from django.conf.urls.static import static
from django.contrib import admin, sitemaps
from django.urls import path, include
from core.views import robots_txt
from django.conf import settings


sitemaps = {
    'application': ApplicationSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('robots.txt', robots_txt, name='robots_txt')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
