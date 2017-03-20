"""Kassandra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
#from Applic.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Applic.urls'))
    #url(r'^$', views.homepage) #r перед адресом - не экранируются никакие символы
    #^ - символ начала строки, $ - символ конца строки
    #второй аргумент -функция, которая отображает страницу по адресу
]
