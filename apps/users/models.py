from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from DjangoUeditor.models import UEditorField
# from datetime import datetime



class Zuozhe(models.Model):
    zuozheNo = models.CharField(max_length=15, verbose_name='作者编号', null=False, blank=False)
    name = models.CharField(max_length=20, verbose_name='作者姓名', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'zuozhe'
        verbose_name = '作者管理'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=15,verbose_name='类别名')
    add_time = models.DateTimeField(verbose_name='生成日期', auto_now_add=True, null=True, blank=True)
    is_tab = models.BooleanField(verbose_name='是否显示',default=True)
    title = models.CharField(max_length=15,verbose_name='题目',default='')
    path_name = models.CharField(max_length=15,verbose_name='种类别名')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name

class TagInfo(models.Model):
    name = models.CharField(max_length=15,verbose_name='标签名')
    add_time = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='生成日期')
    category = models.ForeignKey(Category,null=True,blank=True,verbose_name='类别')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'taginfo'
        verbose_name ='标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章名', null=False, blank=False)
    # content = models.TextField(verbose_name='内容', default='')
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars="full",
                                  imagePath="course/ueditor/", filePath="course/ueditor/",
                                  upload_settings={"imageMaxSize": 1204000},default='')
    sort = models.IntegerField(verbose_name='顺序', default=0)
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    zuozhe = models.ForeignKey(Zuozhe, null=True, blank=True,verbose_name='作者')  # ,related_name='id'
    check_status = models.IntegerField(default=0,verbose_name='审核状态',choices=((0,'审核中'),(1,'审核通过'),(2,'审核失败')))
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间') #default=datetime.now,
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    image = models.TextField(verbose_name='图片',default="static/images/timg.jpg")
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='文章类别')
    tagInfo = models.ForeignKey(TagInfo, null=True, blank=True, verbose_name='文章标签')
    desc = models.TextField(verbose_name='文章简介', default='')
    is_recommend = models.BooleanField(verbose_name='是否推荐', default=False)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'article'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name


class Pic(models.Model):
    pic_name = models.CharField(max_length=15,verbose_name='用户名')
    xuhao = models.IntegerField(verbose_name='xuhao',default=0)
    pic_path = models.TextField(verbose_name='图片路径', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
    modify_time = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.pic_name

    class Meta:
        db_table = 'roll_pic'
        verbose_name = '轮播图管理'
        verbose_name_plural = verbose_name

class User(models.Model):
    username = models.CharField(max_length=15, verbose_name='用户名',null=True,blank=True)
    password = models.CharField(max_length=20, verbose_name='密码',null=True,blank=True)
    nick_name = models.CharField(max_length=15,verbose_name='昵称',null=True,blank=True)
    email = models.CharField(max_length=15, verbose_name='邮箱',null=True,blank=True)
    image = models.ImageField(upload_to='user/upload/', verbose_name='头像图片',null=True,blank=True)
    addtime = models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
    # modify_time = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True,blank=True)
    is_start = models.BooleanField(default=False, verbose_name='激活')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容', null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='生成日期')
    comment_man = models.ForeignKey(User,null=True,blank=True,verbose_name='用户名')
    article = models.ForeignKey(Article,null=True,blank=True,verbose_name='评论的文章')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


    # def __str__(self):
    #     return self.nick_name
    # class Meta:
    #     db_table = 'comment'
    #     verbose_name = '表单验证'
    #     verbose_name_p

# class UserProfile(AbstractUser):
#     nick_name = models.CharField(max_length=15,verbose_name='用户名')
#     # image = models.ImageField(upload_to='user/upload/', verbose_name='头像图片')
#     addtime = models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
#     # modify_time = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True,blank=True)
#     is_start = models.BooleanField(default=False, verbose_name='激活')
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         # db_table = 'userprofile'
#         verbose_name = '用户表'
#         verbose_name_plural = verbose_name


