from django.db import models

# Create your models here.

class Zuozhe(models.Model):
    zuozheNo = models.CharField(max_length=15, verbose_name='作者编号', null=False, blank=False)
    name = models.CharField(max_length=20, verbose_name='作者姓名', null=False, blank=False)
    def __str__(self):
        return self.name
    class Meta():
        db_table = 'zuozhe'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name='文章名',null=False,blank=False)
    content = models.TextField(verbose_name='内容',default='')
    fine = models.BooleanField(verbose_name='是否精华',default=False)
    sort = models.IntegerField(verbose_name='顺序',default=0)
    cli_num = models.IntegerField(default=0, verbose_name='点击量')
    zuozhe = models.ForeignKey(Zuozhe) #,related_name='id'

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'article'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name