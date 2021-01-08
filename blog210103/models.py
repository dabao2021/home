from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=15,verbose_name='用户名')
    image = models.ImageField(verbose_name='头像图片')
    add_time =models.DateTimeField(verbose_name='生成日期',auto_now_add=True,null=True,blank=True)
    # is_start = models.BooleanField(verbose_name='??',)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=15,verbose_name='种类名')
    add_time = models.DateTimeField(verbose_name='生成日期', auto_now_add=True, null=True, blank=True)



