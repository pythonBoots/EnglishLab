"""
Definition of urls for EnglishLab.
"""

from django.conf.urls import include, url
from test_pass import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', EnglishLab.views.home, name='home'),
    # url(r'^EnglishLab/', include('EnglishLab.EnglishLab.urls')),

    # url for test_pass application
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
