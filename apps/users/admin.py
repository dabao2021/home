# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
from users.models import Article
from users.models import Zuozhe


class ArticleXadmin():
    list_display = ['id', 'title', 'content', 'fine', 'sort', 'cli_num','check_status','zuozhe','update_time','create_time']
    list_editable = ['title', 'content','check_status','zuozhe','update_time','create_time']
    # search_fields = ['title', 'content']
    model_icon = 'fa fa-th-list'
    list_per_page = 10

class ZuozheXadmin():
    list_display = ['id', 'zuozheNo', 'name']
    list_editable = ['zuozheNo', 'name']
    model_icon = 'fa fa-address-book-o'  #'fa fa-user'


xadmin.site.register(Article,ArticleXadmin)
xadmin.site.register(Zuozhe,ZuozheXadmin)




