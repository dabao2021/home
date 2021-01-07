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
from datetime import datetime

from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
# from django.urls import path
import xadmin

def index(request):
    category = [{'name': 'python'},{'name':'git'},{'name': 'django'}]
    # print('1111111111',datetime.now())
    return render(request,
                  'index.html', {'all_category': category}
                  )
    # return render(request, 'index.html')

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^$', index, name='user_login'),
    url(r'^$', index, name='user_center'),
    url(r'^$', index, name='user_logout'),
    url(r'^$', index, name='user_register'),
    url(r'^$', index, name='search'),
    url(r'^list', index, name='list'),

    # url(r'^$',index(sitemaps))
]
