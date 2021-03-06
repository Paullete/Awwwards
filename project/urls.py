"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import re_path as url
from rest_framework import routers
from django.contrib import admin
from django.contrib.auth import views
from myproject.views import PostViewset,ProfileViewset
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views  as auth_views




router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewset)
router.register(r'posts', PostViewset)

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'',include('myproject.urls')),
    url('',include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('logout/', auth_views.LogoutView.as_view(next_page = '/')),
    # url(r'^logout/$', views.logout,{"next_page":'/'}),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]