"""blog210103 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
# from django.templatetags import static
from django.template import Context
from django.template.loader import get_template
from django.views import static
import xadmin
# from blog210103 import settings
from users import models

def list_web(request,path):

    return HttpResponse('html')

def detail(request,art_id):

    art = models.Article.objects.filter(id = art_id)#.values('id', 'title','content','desc', 'click_num', 'add_time','image','category')

    print(999999999,art[0].category.name,type(art[0].category.name))

    return render(request,
                  'detail.html', {
                      'art_obj': art[0],
                  }
                  )

def comment(request,art_id):
    return HttpResponse('comment')

def search(request):
    word = request.GET.get("keyword")
    art = models.Article.objects.filter(title__contains = word)#.values('id','title','desc','click_num','add_time','image')
    print (8888888, word)
    # print (8888888, art[0]['title'])
    return render(request,'search_list.html',
        {"all_articles": art,
         }
    )

    # return HttpResponse('html2')
# def home(request):
#     t = get_template("index.html")
#     html = t.render(Context({
#         "template_dir":settings.TEMPLATE_DIRS[0],
#         "title":"Home",
#         "static_dir":settings.STATIC_ROOT}))
#     return HttpResponse(html)

def index(request):
    category = models.Category.objects.filter(is_tab=True).values('name','path_name')
    num = models.Article.objects.count()
    roll_pic = models.Pic.objects.all().values('pic_name','pic_path').order_by('xuhao')
    all_day = 88

    comment = models.Article.objects.filter(is_recommend=True).values('id','title','desc','click_num','add_time','image')
    articles = models.Article.objects.all().order_by('-id') #values('id', 'title', 'desc', 'click_num', 'add_time','image','category').
    print('8888888', num)
    print('9999999', roll_pic)

    return render(request,
                  'index.html', {
                        'all_category': category,
                        'all_bannerpic': roll_pic,
                        'article_total': num,
                        'all_day': all_day,
                        'recommend_article': comment,
                        'all_articles': articles,

                                 }
                  )
    # return HttpResponse(roll_pic)

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^$', index, name='user_login'),
    url(r'^$', index, name='user_center'),
    url(r'^$', index, name='user_logout'),
    url(r'^$', index, name='user_register'),
    url(r'^comment/(?P<art_id>.*)$', comment, name='user_comment'),

    url(r'^detail/(?P<art_id>.*)$', detail, name='detail'),
    url(r'^search/$', search, name='search'),
    url(r'^list/(?P<path>.*)$', list_web, name='list'),
    url(r'static/(?P<path>.*)$',static.serve,{'document_root': settings.STATIC_ROOT},name='media'),
]
