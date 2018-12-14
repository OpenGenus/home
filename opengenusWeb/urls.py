"""opengenusWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from django.views.generic import TemplateView

from pages.views import InternListView,InternDetailView
from pages.sitemaps import SchoolSitemap, InternSitemap, StaticViewSitemap

sitemaps = {
    'schools' : SchoolSitemap,
    'interns' : InternSitemap,
    'static'  : StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
    # path('pages/<int:id>'),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('index', TemplateView.as_view(template_name="index.html"), name="index"),
    path('cosmos', TemplateView.as_view(template_name="cosmos.html"), name="cosmos"),
    path('quark', TemplateView.as_view(template_name="quark.html"), name="quark"),
    path('search', TemplateView.as_view(template_name="search.html"), name="search"),
    path('iq', TemplateView.as_view(template_name="iq.html"), name="iq"),
    path('discuss', TemplateView.as_view(template_name="discuss.html"), name="discuss"),
    # path('intern/<str:username>', internDetailView),
    path('school/', include('schools.urls', namespace="schools")),
    path('intern/', InternListView.as_view(),name='intern'),
    path('intern/<str:slug>', InternDetailView.as_view(),name='intern-detail'),


    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)