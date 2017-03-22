from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader, Context

def homepage(request): #объект, который содержит всю информацию о запросе, объект запроса
	# url = reverse('greet', kwargs = {'name' : 'Lilu'})
	c = Context({'a' : 'Lusinda', 'b' : 'Lilu'})
	name = 'Applic/home.html'
	return render(request, name, c)

# def greet(request, name = None):
# 	return render(request, 'Applic/greet.html', {'name' : name})

	#то же самое, что выше
	# tpl = loader.get_template('Applic/home.html')
	# c = Context({'a' : 'Lusinda'})
	# return HttpResponse(tpl.render(c, request), status = 200, content_type = 'text/html')
	
	#return HttpResponse('', status = 200, content_type = 'text/plain')
#строку возвращать нельзя, только спец.объект, в котором может быть строка
#django/http/response.py
#HttpResponseNotFound
#HttpResponseRedirect и прочие наследники класса
#другие аргументы нужно передавать именованными

#шаблоны
#три типа тегов - для вывода переменных, для выполнения операций, комментарии
#отличия: набор и синтаксис фильтров, допустимые операции
#внутри можно создавать простые значения - строки и числа
#в отличие от джинджи, сумма 2 чисел и т.п. не работает, исп. фильтр add
#фильтр yes, no, maybe
#ifchanged - изменилось ли значение с предыдущей итерации цикла
#{{csrf-token}}, {% csrf-token %} защита от подделки запросов
#способ генерации адресов, связи между функциями и конечными адресами по умолчанию нет, ее нужно создавать вручную

#динам.часть адреса - берем в круглые скобки
#grid
#регулярные выражения; именованные группы
#имена аргументов должны совпадать с именами именованных групп
#reverse_lazy



