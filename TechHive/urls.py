"""
URL configuration for TechHive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
#from home import views
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,),
    path('homepage/',homepage,name='homepage'),
    path('desktop/',desktop),
    path('desktop2/',desktop1),
    path('console/',console),
    path('laptop/',laptop),
    path('laptop2/',laptop2),
    path('monitor/',monitor),
    path('monitor2/',monitor2),
    path('accessories/',accessories),
    path('ac2/',ac2),
    path('gadget/',gadget),
    path('gadget2/',gadget2),
    path('slider/',slider),
    path('component/',component),
    path('component2/',component2),
    path('gaming/',gaming),
    path('gaming_2/',gaming2),
    path('gaming_3/',gaming3),
    path('contact/',contact),
    path('hotdeals/',hotdeals),
    path('hotdeal1/',hotdeal1),
    path('hotdeal2/',hotdeal2),
    path('hotdeal3/',hotdeal3),
    path('login/',login,name='login'),
    path('view_logout/',view_logout),
    path('password_change/',password_change_view),
    path('logout/',logout),
    path('register/',register,name='register'),
    path('header/',header),
    path('footer/',footer),
    path('search', search),
    path('tv/',tv),
    path('phone/', phone),
  # path('login2/',LoginPage,name='login2'),
  # path('home2/',HomePage,name='home2'),
  # path('logout2/',LogoutPage,name='logout2'),
  # path('signup2/',LogoutPage,name='signup2'),
  # path('register2/',register2,name='register2'),
  #password_change
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()