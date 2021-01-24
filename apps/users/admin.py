# from django.contrib import admin
# Register your models here.
from django.db import models
import xadmin
# from users.models import Article
from users import models


class ArticleXadmin():
    list_display = ['id', 'title','desc', 'content', 'is_recommend', 'sort', 'click_num','check_status','image','category','zuozhe','update_time','add_time']
    list_editable = ['title','desc','content','check_status','zuozhe','category','is_recommend','image','update_time','add_time']
    search_fields = ['title', 'content']
    model_icon = 'fa fa-th-list'
    list_per_page = 10
    style_fields = {"content": "ueditor"}

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

class TaginfoXadmin():
    list_display = ['name','category','add_time']
    list_editable = ['name','category']
    model_icon = 'fa fa-picture-o'

class CommentXadmin():
    list_display = ['id','content','comment_man','article','add_time']
    list_editable = ['content','comment_man','article']
    model_icon = 'fa fa-th-list'

class UserXadmin():
    list_display = ['id','username','nick_name','password','image','email','is_start','addtime']
    list_editable = ['username','nick_name','password','image','email','is_start']
    model_icon = 'fa fa-picture-o'


xadmin.site.register(models.Article,ArticleXadmin)
xadmin.site.register(models.Zuozhe,ZuozheXadmin)
xadmin.site.register(models.Pic,PicXadmin)
xadmin.site.register(models.Category,CategoryXadmin)
xadmin.site.register(models.TagInfo,TaginfoXadmin)
xadmin.site.register(models.Comment,CommentXadmin)
xadmin.site.register(models.User,UserXadmin)





