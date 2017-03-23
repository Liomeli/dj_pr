from django.db import models
# Create your models here.

#создание таблицы базы данных

# class Book(models.Model):
# 	title = models.CharField(max_length = 50) #VARCHAR

class Post(models.Model):
 	title = models.CharField(max_length = 50) #VARCHAR	
 #почитать про виды полей Field
 #blank и null, похожи, лучше, чтоб значения были одинаковы
 	content = models.TextField()
 #пробегается только по тем моделям, которые в приложениях, подкл. в settings.py
