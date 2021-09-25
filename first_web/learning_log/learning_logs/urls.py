#coding:utf-8
from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    #main page
    path(r'',views.index,name='index'),
    path(r'topics/',views.topics ,name = 'topics' ),
    path(r'topics/<topic_id>/', views.topic, name='topic'),
    path(r'new_topic/',views.new_topic,name='new_topic'),
    path(r'new_entry/<topic_id>',views.new_entry,name = "new_entry"),
    path(r'edit_entry/<entry_id>',views.edit_entry,name = 'edit_entry')
    ]