"""greenissues URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from apps.bluefish import views

urlpatterns = [
    url(r'^$', views.get_branchinfo, name='get_branchinfo'),
    url(r'^fish/(?P<branch_id>[0-9]+)/$', views.get_changeinfo, name='get_changeinfo'),
    url(r'^fish/$', views.generate_changelist, name='generate_changelist'),
    url(r'^remove/(?P<branch_id>[0-9]+)/$', views.remove_branchinfo, name='remove_branchinfo'),
]
