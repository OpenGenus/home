from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView
from django.conf import settings
from django.urls import path,resolve
from django.conf.urls.static import static

from .views import (SchoolDetailView,SchoolInternView)

app_name = 'schools' 
urlpatterns = [
    path('<slug:url_endpoint>/', SchoolDetailView.as_view(template_name="schools/school_detail.html"), name='detail'),
    path('<slug:url_endpoint>/interns', SchoolDetailView.as_view(template_name="schools/school_listmk.html"), name='asso-interns'),
    # url(r'^create/$', ItemCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/update$', ItemUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
    # url(r'^$', ItemListView.as_view(), name='list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)