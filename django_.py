#python -m django
#django-admin
#django-admin startproject projectname
#wsgi - запускает проект с помощью стороннего сервера
#urls.py - роутер; аналог app.route('/') во flask
#settings.py - настройки приложения
#внутри проекта обычно ничего не создают, делают соседнюю папку(модуль)
#python manage.py runserver - запуск сервера
#python manage.py startapp - создать в проекте новый модуль (приложение)
#создается шаблон проекта, однако каждый новый модуль (приложение), отвечающий
#за отдельную часть сайта, создается отдельно в новой папке, чтобы при отключении
#/удалении одного модуля все остальное продолжало работать

#миграция - разница между текущим состоянием кода и текущим состоянием базы данных
#python manage.py migrate - применение миграций
#python manage.py makemigrations - создание миграций
#python manage.py sqlmigrate Applic 0001 - посмотреть, что делает миграция
#python manage.py shell - интер. консоль
#b.save() - сохранить в базу, где b - объект класса модели
#никогда не менять айди вручную
#b.delete() - удалить объект из базы
#Modelname.objects - метод класса для поиска по базе, доступен только из класса
#o.all - возвр. все записи
#o.get(id = 2) получить элемент с айди = 2, пол. 1 эл., pk - primary key
#o.all[0:5] получ.рез с лимит 0 оффсет 5
#o.filter - фильтр, позв.получить множество эл.
#o.exclude - фильтр наоборот
#o.filter(id__gt = 2) все эл с айди больше 2 или gte больше или равно
#lt	
#o.count - кол-во элементов
#django lookup syntax models/querysets в документации
#идеологически поезд по базе используется только в рамках файла views соотв.функции, не в html
#d__date - метод фильтрации по дате, если поле datetimefield
#is_null = True - проверка на то, что поле является null
#search полнотекстовый поиск, нужно устанавливать доп.библиотеки
#regex искать по регулярным выражениям
#from django.db.models import Q
#c1 = Q(pk__gt = 2) - критерий фильтрации, не привязан к контректному объекту или таблице
#(с1, с2) - с оператором "и
#использовать побитовые операторы: & (и), | (или)
#найти если title = content: сослаться на другое поле
#Q от слова Query, F от слова Field
#title = F('content')
#если нужно получить одну колонку - Post.objects....().values('fieldname')
#aggregate. annotate


#image добавляем в модели
#редактируем html, форма только методом POST + файл кодируется
#enctype = "multipart/form-data"
#request.FILES['fieldname']
#form = PostForm(request.POST, request.FILES)
#def get_image_url() - метод поста
#читать документацию

#class-based view
from django.views.generic import View
class Home(View):

	def get(self, request):
		return render (request, 'home.html')

	def post(self, request):
		return render (request, 'home.html')

#urls - вместо функции homepage - класс Home.as_view()
#TemplateView, RedirectView, DetailedView, ListView, CreateView,
#EditView, UpdateView
#heroku.com - выгрузка сайтаб хостинг
#доменное имя herokuapp.com