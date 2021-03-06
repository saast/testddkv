"""ekl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from kv import views

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'kv.views.home_page', name='home'),
    url(r'estates/$', 'kv.views.estates_page', name='estates'),
    url(r'tenants/$', 'kv.views.tenants_page', name='tenants'),
    url(r'tenants/(?P<tenant_id>[0-9]+)/', 'kv.views.tenant_page', name='tenant'),
    url(r'tenants/new$', 'kv.views.new_tenant', name='new_tenant'),
]
