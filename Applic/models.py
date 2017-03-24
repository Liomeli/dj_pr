from django.db import models
# Create your models here.

#создание таблицы базы данных

# class Book(models.Model):
# 	title = models.CharField(max_length = 50) #VARCHAR

class Post(models.Model):
	
	def __str__(self):
		return ('id = {0}, title = {1}, content = {2}\n'.format(self.id, self.title, self.content))

	#при изменении методов миграцию создавать и сохранять не нужно

	title = models.CharField(max_length = 50) #VARCHAR	
#почитать про виды полей Field
#blank и null, похожи, лучше, чтоб значения были одинаковы
	content = models.TextField()
#пробегается только по тем моделям, которые в приложениях, подкл. в settings.py

class Comment(models.Model):

	body = models.TextField()
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	#CASCADE - при удалении родительского поста удаляются все комментарии
	#SETNULL - при удалении родительского поста установить post как null
	def __str__(self):
		return ('id = {0}, body = {1}, related_post = {2}\n'.format(self.id, self.body, self.post))
#появилось свойство comment_set в каждом классе Post, то же, что и Comment.objects, но из конкретного поста
#comment__body__isnull = True