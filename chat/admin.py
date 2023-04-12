from django.contrib import admin
from chat.models import *
# Register your models here.

@admin.register(Group_names)
class Group(admin.ModelAdmin):
    list_display=('id','name')

@admin.register(Participants)
class Participants(admin.ModelAdmin):
    list_display=('id','name')

@admin.register(Chat)
class Chat(admin.ModelAdmin):
    list_display=('id','msg')


@admin.register(College)
class College(admin.ModelAdmin):
    list_display=('id','name')

