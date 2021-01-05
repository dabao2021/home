# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
from users.models import Article
from users.models import Zuozhe


class ArticleXadmin():
    list_display = ['id', 'title', 'content', 'fine', 'sort', 'cli_num','name']
    list_editable = ['title', 'content']

xadmin.site.register(Article,ArticleXadmin)




