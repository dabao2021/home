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
from users.models import Pic

def list_web(request,path):
    pass

# def home(request):
#     t = get_template("index.html")
#     html = t.render(Context({
#         "template_dir":settings.TEMPLATE_DIRS[0],
#         "title":"Home",
#         "static_dir":settings.STATIC_ROOT}))
#     return HttpResponse(html)

def index(request):
    category = [{'name': 'python','path_name': 'python'},{'name':'git','path_name': 'git'},{'name': 'django','path_name': 'django'}]

    roll_pic = Pic.objects.all().values('pic_name','pic_path').order_by("xuhao")
    print('9999999', roll_pic)

    return render(request,
                  'index.html', {'all_category': category,
                                 'all_bannerpic': roll_pic,
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
    url(r'^$', index, name='search'),
    url(r'^list/(?P<path>.*)$', list_web, name='list'),
    url(r'static/(?P<path>.*)$',static.serve,{'document_root': settings.STATIC_ROOT},name='media'),
]
