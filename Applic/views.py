from django.shortcuts import render
from django.http import HttpResponse

def homepage(request): #объект, который содержит всю информацию о запросе, объект запроса
	return HttpResponse('hello', status = 200, content_type = 'text/plain')
#строку возвращать нельзя, только спец.объект, в котором может быть строка
#django/http/response.py
#HttpResponseNotFound
#HttpResponseRedirect и прочие наследники класса

# Create your views here.
