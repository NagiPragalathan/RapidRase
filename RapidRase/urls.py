"""
URL configuration for RapidRase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from RapidRase import settings
from django.conf.urls.static import static

from base.Views.Admin import *

from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = []

admin.site.site_header = "RapidRase"

admin_url = [
    path('admin/', admin.site.urls),

]

Repath = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

Details_urls = [
    path('', details_list, name='details_list'),
    path('details/add/', details_create_edit, name='details_create_edit'),
    path('details/edit/<uuid:uuid>/', details_create_edit, name='details_create_edit'),
    path('details/delete/<uuid:uuid>/', details_delete, name='details_delete'),
    path('details/<uuid:details_uuid>/upload_image/', image_upload, name='image_upload'),
    path('details/<uuid:uuid>/', detail_view, name='detail_view'),

    path('details/<uuid:details_uuid>/upload_image/', image_upload, name='image_upload'),
    path('image/delete/<int:image_id>/', image_delete, name='image_delete'),
]

urlpatterns.extend(Repath)
urlpatterns.extend(Details_urls)
urlpatterns.extend(admin_url)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()