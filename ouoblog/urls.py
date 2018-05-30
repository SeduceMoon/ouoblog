"""ouoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from ouo.view.login import login
from ouo.view.views import index, addData, zt, arti, add_arti, upload_img, addwz, wzgl, scwz

from django.urls import path

urlpatterns = [
    path('', login, ),
    path('ly', addData, ),
    path('index', index, ),
    path('zt', zt, ),

    # 文章阅读
    path('arti', arti, ),
    # 编辑界面
    path('add', add_arti, ),
    # 上传文章
    path('add_wz', addwz, ),
    # 删除文章
    path('scwz', scwz, ),
    # 文章管理
    path('wzgl', wzgl, ),
    # 上传图片
    path('uploaddata', upload_img, ),
]
