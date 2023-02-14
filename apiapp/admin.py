from django.contrib import admin
from .models import MyUser, Task


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'roles']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to']


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Task, TaskAdmin)
