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
# from datetime import datetime

from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.views import static
import xadmin
from users import views
from django.views.static import serve


    # return HttpResponse('html2')
# def home(request):
#     t = get_template("index.html")
#     html = t.render(Context({
#         "template_dir":settings.TEMPLATE_DIRS[0],
#         "title":"Home",
#         "static_dir":settings.STATIC_ROOT}))
#     return HttpResponse(html)


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='user_login'),
    url(r'^$', views.index, name='user_center'),
    url(r'^$', views.index, name='user_logout'),
    url(r'^$', views.index, name='user_register'),
    url(r'^comment/(?P<art_id>.*)$', views.comment, name='user_comment'),

    url(r'^detail/(?P<art_id>.*)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^list/(?P<path>.*)$', views.list_web, name='list'),
    url(r'static/(?P<path>.*)$',static.serve,{'document_root': settings.STATIC_ROOT},name='static'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT},name='media')
]
