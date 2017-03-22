from django.db import models
# Create your models here.

#создание таблицы базы данных

class Book(models.Model):
	title = models.CharField(max_length = 50) #VARCHAR
