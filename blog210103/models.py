from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=15,verbose_name='用户名')
    image = models.ImageField(verbose_name='头像图片')
    add_time = models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
    modify_time = models.DateTimeField(verbose_name='修改日期',auto_add=True,null=True,blank=True)
    # is_start = models.BooleanField(verbose_name='??',)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=15,verbose_name='类别名')
    add_time = models.DateTimeField(verbose_name='生成日期', auto_now_add=True, null=True, blank=True)
    path_name = models.CharField(max_length=15,verbose_name='种类别名')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class Pic(models.Model):
    pic_name = models.CharField(max_length=15,verbose_name='用户名')
    xuhao = models.IntegerField(verbose_name='xuhao',default=0)
    pic_path = models.TextField(verbose_name='图片路径', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
    modify_time = models.DateTimeField(verbose_name='修改日期',auto_add=True,null=True,blank=True)


    def __str__(self):
        return self.pic_name

    class Meta:
        db_table = 'roll_pic'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name



