from itertools import chain

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from s_app.models import Category, Service
from s_app.forms import ServiceForm, SearchForm

from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.views.generic.base import View

# Create your views here.

def index(request):
    return HttpResponse("<h1>jfiokweofkwoweko</h1>")

def page(request):
    return HttpResponse("<h2>Страница сiejity текстом</h2>")

def static_page(request):
    return render(request,'s_app/page1.html',)



def main(request):
    data = Category.objects.all()
    return render(request,'s_app/main.html',{'data': data})

def about(request):
    data = Category.objects.all()
    return render(request,'s_app/about.html',{'data': data})

def services(request):
    data = Category.objects.all()
    return render(request,'s_app/services.html',{'data': data})

def gallery(request):
    data = Category.objects.all()
    return render(request,'s_app/gallery.html',{'data': data})

def contact(request):
    data = Category.objects.all()
    data1 = dict()
    data1['timework'] = 'ежедневно с 9-00 до 21-00'
    data1['address'] = 'город Минск, проспект Мира, 1'
    data1['tel'] = '+375291234567'
    data1['email'] = 'salonkrasotysky@gmail.com'
    return render(request, 's_app/contact.html', {'data': data, 'data1': data1})

def showservice(request, id):
    data = Category.objects.all()
    dataservice = Service.objects.get(id=id)
    return render(request, 's_app/service.html', {'data': data, 'dataservice': dataservice})

def showcategory(request, id):
    data = Category.objects.all()
    category = Category.objects.get(id=id)
    data2 = Service.objects.filter(category=category)
    return render(request, 's_app/showcategory.html', {'data': data, 'data2': data2})


def review(request):
    data = Category.objects.all()
    data3 = Service.objects.filter(user=request.user)
    return render(request, 's_app/review.html', { 'data': data, 'data3': data3})

def add_item(request):
    data = Category.objects.all
    form = ServiceForm()
    msg = ''
    if request.method == 'POST':
        category = Category.objects.get(id = request.POST['category'])
        service = Service.objects.create(text=request.POST['text'], title=request.POST['title'], image=request.FILES ['image'], category=category, user=request.user)
        service.save()
        #form = ServiceForm(request.POST,request.FILES)
        #if form.is_valid():
            #form.save()
        msg = 'ok'

    return render(request, 's_app/add_item.html', {'form': form, 'data': data, 'msg': msg})


class RegisterFormView(FormView):
    data = Category.objects.all
    form_class = UserCreationForm
    success_url = "/main"
    template_name = "s_app/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    data = Category.objects.all
    form_class = AuthenticationForm
    template_name = "s_app/login.html"
    success_url = "/main"

    def form_valid(self, form):
        self.user=form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')

def search(request):
    data = Category.objects.all
    data2 = Service.objects.all
    form = SearchForm()
    data1 = []
    if request.method == 'POST':
        if request.POST['where'] == '1' and request.POST['count'] == '0':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'])
        elif request.POST['where'] == '2' and request.POST['count'] == '0':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'])
        elif request.POST['where'] == '0' and request.POST['count'] == '1':
            data1 = Service.objects.filter(category__gt=request.POST['price_edit'])
        elif request.POST['where'] == '0' and request.POST['count'] == '1':
            data1 = Service.objects.filter(category__lt=request.POST['price_edit'])
        elif request.POST['where'] == '1' and request.POST['count'] == '2':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'],
                                           text__lt=int(request.POST['price_edit']))
        elif request.POST['where'] == '2' and request.POST['count'] == '2':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'],
                                           text__lt=int(request.POST['price_edit']))
        elif request.POST['where'] == '1' and request.POST['count'] == '1':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'],
                                           text__lt=int(request.POST['price_edit']))
        elif request.POST['where'] == '2' and request.POST['count'] == '1':
            data1 = Service.objects.filter(title__icontains=request.POST['searchtext'],
                                           text__lt=int(request.POST['price_edit']))
    return render(request, 's_app/search.html', {'data': data, 'form': form, 'data1': data1, 'data2': data2})

def get_item_one(request, id):
    data = Category.objects.all()
    data2 = Service.objects.get(id=id)
    return render(request, 's_app/get_item_one.html', {'data': data, 'data2': data2})

def update_item(request, id):
    data = Category.objects.all()
    obj = Service.objects.get(id=id)
    form = ServiceForm(instance=obj)

    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        Service.objects.filter(id=id).update(text=request.POST['text'], title=request.POST['title'], category=category)
        #form = ServiceForm(request.POST, request.FILEs, instance=obj)
        #if form.is_valid():
            #form.save()
            #Service.objects.filter(id=id)
        return redirect('review')

    return render(request, 's_app/update_item.html', {'data': data, 'form': form})


def delete_item(request, id):
    obj = Service.objects.get(id=id).delete()
    return redirect('review')



