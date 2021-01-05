# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
from users.models import Article


class ArticleXadmin():
    list_display = ['id','title']
    list_editable = ['title',]
xadmin.site.register(Article,ArticleXadmin)




