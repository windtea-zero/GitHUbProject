"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from blog.urls import views
from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from blog.feed import LatestEntriesFeed
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modified_time'
}
urlpatterns = [

                  url(r'^$', views.index),
                  url(r'^admin/', admin.site.urls),
                  url(r'^blog/', include('blog.urls')),
                  url(r'^latest/feed/$', LatestEntriesFeed()),
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
                      name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
