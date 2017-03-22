from django.conf.urls import url
from . import views

urlpatterns = [
	url('applic/$', views.homepage)
]


#name - имя роута
#app.name - название приложения
#динам.часть адреса