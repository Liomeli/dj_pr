from django.shortcuts import render, redirect #аналог нижнего редирект

from django.template import loader, Context
from .models import Post
from django.db.models import Q, F


import django.forms as forms

class MyForm (forms.Form):
	title = forms.Charfield(max_length = 20)
	content = forms.TextField(widget = forms.Textarea) #параметр validators
#form.as_table, as_ul, as_p

#в таком варианте вся логика формы на стороне движка, нельзя сломать сайт, удалив что-то в html

# class PostForm (forms.ModelForm):
# 	title = forms.Charfield(max_length = 20)
# 	content = forms.TextField(widget = forms.Textarea)
	


def homepage(request): 
	# name = 'Applic/home.html'
	form = MyForm() #{'title' : 'sdfsdfsdf', 'content' : 'dfgdfgdfgfdg'} проходит валидация, initial не валидируется
	return render(request, 'home.html', {'form' : form})

#if form.is_valid:
	#form.data['title'] или
	#form.cleaned_data['title'] оставляет тип данных поля, не преобразовывая в строку

	#Post(**form.cleaned_data).save()
	#return redirect

#class X (forms.ModelForm):
#	class Meta:
#	model = Post
#	fields = ['title', 'content']
#настройка формы на основании модели, с которой она изначально связана
#django сам решает, как создать форму
#fields.__all__ - форма со всеми колонками модели