import os

from django.core.paginator import Paginator
from django.db.models import Q,F,Count
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

from article.settings import BASE_DIR
from wenzhang.models import Article
import json
import pymysql

# Create your views here.

def add_arti(request):
    for i in range(1,36):
        Article.objects.get_or_create(title="文章题目"+str(i),content="文章内容"+str(i))
    return HttpResponse("添加35篇文章完成")

#删除文章
def del_arti(request):
    Article.objects.filter(id__gte = 30).delete()
    return HttpResponse("删除文章完成")

#修改点击量
def alter(request):
    # Article.objects.all().update(cli_num = F('cli_num')+100)把所有点击率加100
    Article.objects.filter(Q(sort=1)|Q(title__contains='2')).update(cli_num=F('cli_num') + 100)
    print(Article.objects.all().count())
    # list1 = list((Article.objects.all().values("cli_num")))
    # for i in range(len(list1)):
    #     Article.objects.all().update(cli_num = list1[i]['cli_num']+100)
    Article.objects.all().values('id').annotate(count=Count('content')).values('id',
                                                                                     'count').query.__str__()
    return HttpResponse("修改成功")


#1、获取2篇推荐文章
def fine_arti(request):
    obj = Article.objects.filter(fine = 1).values('title','content')


    # list1 = []
    # for i in obj[0:3]:
    #     list1.append({"title":i.title,"content":i.content})
    #
    # js = json.dumps(list1,ensure_ascii=False,indent=4)
    # print('js:', js)

    js = json.dumps(list(obj),ensure_ascii=False,indent=4)#content_type="application/json",
    print(js)
    return HttpResponse(js)

    # dict0 = {}
    # dict0["xuhao"] = js
    # return JsonResponse(list(obj),safe=False,json_dumps_params={"ensure_ascii":False})



#2、提取10篇文章
def  show_arti(request):
    p = int(request.GET.get("page"))
    # print (p,type(p))
    # start = 10*(p-1)
    # end = 10*p
    # obj = Article.objects.all()[start:end]
    # list1 = []
    # for i in obj:
    #     # print (type(i.content),i.content)
    #     list1.append({"title":i.title,"content":i.content})
    # js = json.dumps(list1, ensure_ascii=False,indent=4)
    # print(list1)
    # print(js)
    obj = Article.objects.all().values('title','content','cli_num').order_by("title")
    obj_page = Paginator(list(obj),10)
    page10 = obj_page.page(p)
    print (type(page10),page10)
    return JsonResponse(list(page10),safe=False,json_dumps_params={"ensure_ascii":False})

#3、文章搜索
def search_arti(request):
    # s = input('要搜索的内容是：')
    sc = request.GET.get("search")
    obj = Article.objects.filter(title__contains=sc)
    # print (obj,type(obj),len(obj))
    #
    if len(obj):
        print ('搜到', len(obj), '篇文章：')
        list1 = []
        for i in obj:
            list1.append({"title": i.title, "content": i.content})
        js = json.dumps(list1, ensure_ascii=False, indent=4)
        return HttpResponse(js)
    else:
        return HttpResponse("<script> alert(\"对不起，没有搜到文章！\");</script> ")

def show1(request):
    db = pymysql.connect("localhost","root","adminDB","wenzhang")
    cursor = db.cursor()
    cursor.execute("select * from article")
    data = cursor.fetchone()
    print(data)
    db.close()

def show_render(request):
    a = os.path.join(BASE_DIR,'templates')
    list1 = [a]
    print ('111111',a)
    return render(request,'index.html',{'n':list1})
