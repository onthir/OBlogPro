"""oblogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include  # Use path and re_path instead of url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from master.views import BlogSitemap

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/auth/site-control/', admin.site.urls),  # Use path for standard URLs
    path('', include('master.urls')),  # Root URL for 'master' app
    path('downloads/', include('download.urls')),  # Path for 'download' app
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  # Use re_path for regex URL patterns
]

