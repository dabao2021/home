# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
# from users.models import Article
from users import models


class ArticleXadmin():
    list_display = ['id', 'title', 'content', 'fine', 'sort', 'cli_num','check_status','zuozhe','update_time','create_time']
    list_editable = ['title', 'content','check_status','zuozhe','update_time','create_time']
    search_fields = ['title', 'content']
    model_icon = 'fa fa-th-list'
    list_per_page = 10

class ZuozheXadmin():
    list_display = ['id', 'zuozheNo', 'name']
    list_editable = ['zuozheNo', 'name']
    model_icon = 'fa fa-address-book-o'  #'fa fa-user'
class PicXadmin():
    list_display = ['pic_name', 'xuhao', 'pic_path', 'create_time', 'modify_time']
    list_editable = ['pic_name', 'xuhao','pic_path', 'create_time']
    search_fields = ['pic_name']
    model_icon = 'fa fa-picture-o'
    list_per_page = 10

xadmin.site.register(models.Article,ArticleXadmin)
xadmin.site.register(models.Zuozhe,ZuozheXadmin)
xadmin.site.register(models.Pic,PicXadmin)





