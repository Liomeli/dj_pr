from django.conf.urls import url
from . import views

urlpatterns = [
	url('home/$', views.homepage)
]


#name - имя роута
#app.name - название приложения
#динам.часть адреса