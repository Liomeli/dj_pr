from django.conf.urls import url
from . import views

urlpatterns = [
	url('home/$', views.homepage, name = 'homepage')
]


#name - имя роута
#app.name - название приложения
#динам.часть адреса
#в адресе можно использовать регулярные выражения (группы в скобках),
#тогда доп.аргументы по количеству скобок передаются в функцию в views.py