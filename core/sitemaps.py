from django.contrib.sitemaps import Sitemap
from core.models import ApplicationModel
from django.shortcuts import reverse


class ApplicationSitemap(Sitemap):
    def items(self):
        return ApplicationModel.objects.all()