from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
# 데이터베이스에 연결하는 방법 -- admin 페이지에!
admin.site.register(ToDoList)
admin.site.register(Item)
