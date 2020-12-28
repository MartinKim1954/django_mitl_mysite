from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # render안에 딕셔너리 형태로 값을 패스할 수 있음! 
    # 딕셔너리 '키'는 html에서 받을 값
    # value에 받을 값
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})
