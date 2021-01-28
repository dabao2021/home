from django import forms
from django.contrib.auth import login
from django.contrib.auth import authenticate
# from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog210103.settings import STATIC_URL, MEDIA_URL
from users import models
import datetime
import hashlib

# Create your views here.
def iPagination(params):
    import math

    ret = {
        "is_prev":1,
        "is_next": 1,
        "from": 0,
        "end": 0,
        "current": 0,
        "total_pages": 0,
        "page_size": 0,
        "total": 0,
        "url":params['url']
    }
    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    display = int(params['display'])
    total_pages = int(math.ceil( total/page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2))

    if page - semi > 0 :
        ret['from'] = page -semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end']+1)
    return  ret

def list_web(request,path):
    tag_temp = request.GET.get("tag")


    cate_obj = models.Category.objects.filter(path_name=path)[0]
    # art = models.Article.objects.filter(category_id=a[0].id)
    art = cate_obj.article_set.all()
    category = models.Category.objects.filter(is_tab = 1)
    tag = cate_obj.taginfo_set.all()
    # tag = models.TagInfo.objects.all()
    # print(7777777,MEDIA_URL)
    if tag_temp:
        # art = cate_obj.article_set.filter(tagInfo_id=int(tag_temp))
        return render(request,'list.html',
                  {
                    'all_articles': art,
                    'all_tags': tag,
                    'all_category':category,
                    'cate_obj':cate_obj,
                    # 'MEDIA_URL': MEDIA_URL,
                  }
                  )
    else:
        # art = cate_obj.article_set.filter(tagInfo_id=int(tag_temp))
        return render(request, 'list.html',
                      {
                          'all_articles': art,
                          'all_tags': tag,
                          'all_category': category,
                          'cate_obj': cate_obj,
                          # 'MEDIA_URL': MEDIA_URL,

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
    comment_list = models.Comment.objects.filter(article=art)
    return render(request,
                  'detail.html', {
                      'art_obj': art[0],
                      'all_category': category,
                      'all_tags':tag,
                      'user_comment_list':comment_list

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

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'required':'邮箱必填'})
    password = forms.CharField(min_length=2,required=True,error_messages={'required':'密码必填'})
    nick_name = forms.CharField(min_length=2,required=True,error_messages={'required':'昵称必填'})

def user_register(request):

    if request.method == 'GET':
        return render(request, 'user_register.html')
    else:
        form = RegisterForm(request.POST)
        #邮箱已注册把已存在信息报给注册模板
        print('form.is_valid:',form.is_valid())
        print(form.errors)
        # #点击注册进入user_register.html模板：
        # if (e_mail is None) or (nick_name is None) or (password is None):
        #     return render(request, 'user_register.html')
        #注册信息检验通过：
        if form.is_valid():

            e_mail = form.cleaned_data['email']
            nick_name = form.cleaned_data['nick_name']
            password = form.cleaned_data['password']
            user = models.User.objects.filter(email=e_mail)
            if user:
                return render(request, 'user_register.html', {'msg': '邮箱已存在'})
            #md5加密
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            print(m.hexdigest())
            #通过ORM写入数据库
            user_obj = models.User.objects.create(email=e_mail, nick_name=nick_name, password=m.hexdigest())
            category = models.Category.objects.filter(is_tab=True).values('name', 'path_name', 'id')
            return render(request,'wait_start.html',
                    {'all_category':category,
                     'user_obj':user_obj,
                    }
                    )
        #如果校验不通过，把错误信息报给注册模板
        else:
            return render(request, 'user_register.html', {'register_form': form, })



    # if (email is None) or (nick_name is None) or (password is None) :
    #     return render(request, 'user_register.html')
    # elif (email == '') or (nick_name == '') or (password == ''):
    #     return render(request, 'user_register.html',{'register_form':form,})
    # else:
    #     user_obj = models.User.objects.create(email=email, nick_name=nick_name, password=password)
    #     category = models.Category.objects.filter(is_tab=True).values('name', 'path_name', 'id')
    #
    #     return render(request,'wait_start.html',
    #             {'all_category':category,
    #              'user_obj':user_obj,
    #             }
    #             )

#构建用于“登录视图”的验证表单类
class LoginForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'required':'邮箱必填'})
    password = forms.CharField(required=True,error_messages={'required':'密码必填'})
#登录视图
def user_login(request):
    if request.method == 'GET':#Get传递的情况
        return render(request, 'user_login.html')
    else:#post传递的情况
        form = LoginForm(request.POST)

        # 点击登录进入user_login.html模板：
        if form.is_valid():
            e_mail = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user0 = models.User.objects.filter(email=e_mail)

            #假设用户不存在
            if user0.count()==0:
                return render(request, 'user_login.html', {'msg': '用户不存在', })
            #假设用户存在，比较密码一致性
            else:
                m = hashlib.md5()
                m.update(password.encode('utf-8'))
                # user0 = authenticate(username=e_mail, password=password)
                print(7777777777777, type(user0[0]), user0[0])

                if user0[0].password == m.hexdigest():
                    # user0= {'username':'bobo',
                    # 'is_authenticated':'1'}
                    print(888888888888888, password)
                    login(request,user0[0])
                    print(999999999999999, m.hexdigest())
                    return redirect('/')
                else:
                    return render(request, 'user_login.html', {'msg': '密码错误', })
        else:
            return render(request, 'user_login.html', {'loginform': form, })

#主页视图
def index(request):
    category = models.Category.objects.filter(is_tab=True).values('name','path_name','id')
    roll_pic = models.Pic.objects.all().values('pic_name','pic_path').order_by('xuhao')
    num = models.Article.objects.count()

    today = datetime.datetime.now()#.strftime("%Y-%m-%d")
    # print(111111111,today)
    old_day = datetime.datetime(2019,12,31)
    all_day = str(today - old_day).split(" days",2)[0]

    # print(22222222222,all_day)
    comment = models.Article.objects.filter(is_recommend=True).values('id','title','desc','click_num','add_time','image')
    articles = models.Article.objects.all().order_by('-id') #values('id', 'title', 'desc', 'click_num', 'add_time','image','category').
    tag = models.TagInfo.objects.all()

    new_comment_art = models.Comment.objects.all().order_by('-id').values('article_id')#.distinct()#
    a = list(new_comment_art)
    new_art = []
    for i in new_comment_art:
        if i in new_art:
            continue
        else:
            new_art.append(i)

    # print(11111111,new_art)
    art_all = []
    for j in new_art:
        art_item = models.Article.objects.filter(id=j['article_id'])
        art_all.append(art_item[0])
    # print(art_all)
            # print(new_art_obj)
        # new_art = new_art.append(new_art_obj[0])

    # new_art.append('0')
    # print('new_art:',new_art)
    # print('new_comment_art:::::',new_comment_art[0].id)
    # for i in new_comment_art:
    #     new_art_obj = models.Article.objects.filter(id=i.id)#.values('title','id','image','add_time','click_num')
    #     # print(new_art_obj)
    #     new_art = new_art.append(new_art_obj[0])
    #
    # print('new_art::::',new_art)

    # print('8888888tag',tag[0].article_set.count())
    # print ('MEDIA_URL:',MEDIA_URL)
    # cont_num = articles.comment.count()

    article_total = articles.count()
    page = int((request.GET.get('p',1)))
    page_params = {
        'total':article_total,
        'page_size':5,
        'page':page,
        'display':4,
        'url':request.path.replace('&p={}'.format(page),'?')

    }
    pages = iPagination(page_params)
    return render(request,
                  'index.html', {
                        'all_category': category,
                        'all_bannerpic': roll_pic,
                        'article_total': num,
                        'all_day': all_day,
                        'recommend_article': comment,
                        'all_articles': articles,
                        'cate_name': tag,
                        'pages':pages,
                        'new_articles':art_all,


                        # 'cont_num':cont_num
                        # 'MEDIA_URL':MEDIA_URL

                                 }
                  )
    # return HttpResponse(roll_pic)

# def user_register(request):
#     email = request.POST.get('email')
#     nick_name = request.POST.get('nick_name')
#     password = request.POST.get('password')
#     if email:
#         print('email is ok')
#         user_obj = models.User.objects.create(email=email,nick_name=nick_name,password=password)
#         return HttpResponse(user_obj.nick_name+"注册成功")
#         # else:
#         #     return HttpResponse("没有注册成功请重新注册"+"<a href= '#/register'>")
#     else:
#         print('email is null')
#         return HttpResponse("没有注册成功请重新注册" + "<a href= ''>点击重新注册</a>")
#
#     return render(request,'user_register.html',
#             {
#             }
#             )