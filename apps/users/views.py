from django.http import HttpResponse
from django.shortcuts import render
from users import models
import datetime


# Create your views here.



def list_web(request,path):
    cate_obj = models.Category.objects.filter(path_name=path)[0]
    # art = models.Article.objects.filter(category_id=a[0].id)
    art = cate_obj.article_set.all()
    category = models.Category.objects.filter(is_tab = 1)
    tag = cate_obj.taginfo_set.all()
    # tag = models.TagInfo.objects.all()
    # print(7777777,a[0])

    return render(request,'list.html',
                  {
                    'all_articles': art,
                    'all_tags': tag,
                    'all_category':category,
                    'cate_obj':cate_obj,

                  }
                  )
    # return HttpResponse('html')


def detail(request,art_id):

    art = models.Article.objects.filter(id = art_id)#.values('id', 'title','content','desc', 'click_num', 'add_time','image','category')
    category = models.Category.objects.filter(is_tab=True).values('name', 'path_name')
    print(999999999,art[0].category.name,type(art[0].category.name))
    #标签云相关
    tag = models.TagInfo.objects.filter(category_id=art[0].category_id)
    # tag = models.TagInfo.objects.all()
    return render(request,
                  'detail.html', {
                      'art_obj': art[0],
                      'all_category': category,
                      'all_tags':tag,
                  }
                  )

def comment(request,art_id):
    return HttpResponse('comment')

def search(request):
    category = models.Category.objects.filter(is_tab=True).values('name', 'path_name', 'id') #list表



    word = request.GET.get("keyword")
    art = models.Article.objects.filter(title__contains = word)#.values('id','title','desc','click_num','add_time','image')
    tag = models.TagInfo.objects.all()#标签云
    # tag = models.TagInfo.objects.filter(category_id=art[0].category_id)#标签云过滤
    print (8888888, word,len(art))
    # print (8888888, art[0]['title'])
    if len(art) == 0:
        return render(request, 'none.html',
                      {
                       'all_category': category,
                       }
                      )
    else:
        return render(request,'search_list.html',
            {"all_articles": art,
             'all_category': category,
             'all_tags': tag,
            }
            )


def index(request):
    category = models.Category.objects.filter(is_tab=True).values('name','path_name','id')
    roll_pic = models.Pic.objects.all().values('pic_name','pic_path').order_by('xuhao')
    num = models.Article.objects.count()
    today = datetime.datetime.now()#.strftime("%Y-%m-%d")
    print(111111111,today)
    old_day = datetime.datetime(2019,12,31)
    all_day = str(today - old_day).split(" days",2)[0]
    print(22222222222,all_day)
    comment = models.Article.objects.filter(is_recommend=True).values('id','title','desc','click_num','add_time','image')
    articles = models.Article.objects.all().order_by('-id') #values('id', 'title', 'desc', 'click_num', 'add_time','image','category').
    tag = models.TagInfo.objects.all()

    return render(request,
                  'index.html', {
                        'all_category': category,
                        'all_bannerpic': roll_pic,
                        'article_total': num,
                        'all_day': all_day,
                        'recommend_article': comment,
                        'all_articles': articles,
                        'cate_name': tag

                                 }
                  )
    # return HttpResponse(roll_pic)