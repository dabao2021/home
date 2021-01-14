# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
# from users.models import Article
from users import models


class ArticleXadmin():
    list_display = ['id', 'title','desc', 'content', 'is_recommend', 'sort', 'click_num','check_status','category','zuozhe','update_time','add_time']
    list_editable = ['title','desc','content','check_status','zuozhe','category','is_recommend','update_time','add_time']
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
class CategoryXadmin():
    list_display = ['name','path_name','is_tab','title','add_time']
    list_editable = ['name','title','is_tab','path_name']
    model_icon = 'fa fa-th-list'

xadmin.site.register(models.Article,ArticleXadmin)
xadmin.site.register(models.Zuozhe,ZuozheXadmin)
xadmin.site.register(models.Pic,PicXadmin)
xadmin.site.register(models.Category,CategoryXadmin)





