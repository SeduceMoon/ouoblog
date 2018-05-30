# coding utf-8
import json
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from ouo.models.models import LY, USER, WZ
from ouo.utils.utils import fileNum, wzInfal


# 主界面 包含随机用户session
def index(request):
    user = request.GET.get("user")
    cursor = USER.objects.filter(name=user)
    if cursor.count() != 0:
        request.session["name"] = user
        data = open(os.getcwd() + "/ouoblog/data.dt").read()
        return render(request, "0o0/index.html", {"dmdata": data.replace("\n", "")})
    else:
        return HttpResponse("用户名不存在")


# 留言数据添加
def addData(request):
    if (request.session.exists(request.session.session_key)):
        data1 = str(request.body, "utf-8")
        try:
            LY.objects.create(name="test", data=data1, userid="0")
            return HttpResponse("ok")
        except Exception:
            return HttpResponse("error")
            pass
    else:
        return HttpResponse("error")


# 专题页面
def zt(request):
    if (request.session.exists(request.session.session_key)):
        data = ""
        name = str(request.GET.get("name")).replace(" ", "")
        querySet = WZ.objects.filter(wz_by1=name)  # type QuerySet
        for i in range(0, querySet.count()):
            item = loader.get_template('item/zt_item.html')
            con = {"showid": "" + str(i + 1), "showtitle": querySet[i].wz_name,
                   "showtime": time.strftime("%Y-%m-%d\n···T:%H:%M:%S", time.localtime(float(querySet[i].wz_time)))}
            data += str(item.render(con))
        return render(request, "0o0/zt.html", {"show_all_item": data, "zt_name": name})
    else:
        return HttpResponse("请先前往首页登录登录http://ishabing.club")


# 文章阅读器界面
def arti(request):
    if (request.session.exists(request.session.session_key)):
        print(request.POST.get("index"))
        print(request.POST.get("wz_name"))
        data = WZ.objects.filter(
            wz_by1=request.POST.get("index"),
            wz_name=request.POST.get("wz_name")
        )
        return render(request, "0o0/show_wz.html",
                      {"zt_name": data[0].wz_by1, "wz_name": data[0].wz_name, "zz_name": data[0].wz_zz,
                       "wz_nr": data[0].wz_nr})
    else:
        return HttpResponse("请先前往首页登录登录http://ishabing.club")


# 添加文章
def add_arti(request):
    if (request.session.exists(request.session.session_key)):
        return render(request, "0o0/add_wz.html")
    else:
        return HttpResponse("请先前往首页登录登录http://ishabing.club")


# 删除文章
def scwz(request):
    if request.method == "POST":
        if (request.session.exists(request.session.session_key)):
            try:
                wzmc = request.POST.get("wz_mc")
                wzzt = request.POST.get("wz_zt")
                WZ.objects.filter(wz_name__iendswith=wzmc, wz_by1=wzzt).delete()
                return HttpResponse("ok")
            except Exception:
                return HttpResponse("error")
        else:
            return HttpResponse("error")
    return HttpResponse("error")


# 文章管理
def wzgl(request):
    if (request.session.exists(request.session.session_key)):
        data = ""
        type = request.POST.get("type")
        if type == None:
            type = "nofind"
        value = request.POST.get("value")
        if value == None:
            value = "因为一个人爱上一座城"
        if value == "*":
            qs = WZ.objects.all()
            for qs_item in qs:
                item = loader.get_template("item/wzgl_item.html")
                con = {"name": qs_item.wz_name, "zt_name": qs_item.wz_by1}
                data += str(item.render(con))
        if type == "find" and value != "*":
            qs = WZ.objects.filter(wz_name__iendswith=value)
            for qs_item in qs:
                item = loader.get_template("item/wzgl_item.html")
                con = {"name": qs_item.wz_name, "zt_name": qs_item.wz_by1}
                data += str(item.render(con))
        elif type == "nofind" and value != "*":
            qs = WZ.objects.filter(wz_by1=value)
            for qs_item in qs:
                item = loader.get_template("item/wzgl_item.html")
                con = {"name": qs_item.wz_name, "zt_name": qs_item.wz_by1}
                data += str(item.render(con))
        return render(request, "0o0/wz_gl.html", {"wz_lb": data})
    else:
        return HttpResponse("请先前往首页登录登录http://ishabing.club")


# 添加文章图片上传
@csrf_exempt
def upload_img(request):
    if (request.session.exists(request.session.session_key)):
        file_obj = request.FILES.get('img', None)
        file_name = os.getcwd() + "/ouo/static/img/imgdata/" + fileNum(os.getcwd() + "/ouo/static/img/imgdata")
        with open(file_name, mode='wb') as f:
            f.write(file_obj.read())
            f.flush()
            f.seek(0)
        return HttpResponse(
            json.dumps({"errno": 0, "data": ["http://127.0.0.1:8000/static/img/imgdata/" + file_name.split("/")[-1]]}))
    else:
        return json.dumps({"errno": 1, "data": "请先前往首页登录登录http://ishabing.club"})


def addwz(request):
    if (request.session.exists(request.session.session_key)):
        wz_nr = wzInfal(request.POST.get("wz_nr"))
        wz_by1 = wzInfal(request.POST.get("wz_by1"))
        wz_name = "NO:" + str(WZ.objects.filter(wz_by1=wz_by1).count() + 1) + "··" + request.POST.get("wz_name")
        # wz_name ="··" + request.POST.get("wz_name")
        wz_zzjy = request.POST.get("wz_zzjy")
        wz_zz = request.POST.get("wz_zz")
        wz_time = time.time()
        wz_dz = 0
        wz_lll = 0
        try:
            WZ.objects.create(wz_dz=wz_dz, wz_nr=wz_nr, wz_name=wz_name, wz_zzjy=wz_zzjy, wz_zz=wz_zz, wz_time=wz_time,
                              wz_lll=wz_lll, wz_by1=wz_by1)
            return HttpResponseRedirect("add")
        except Exception:
            return HttpResponse("error")
    else:
        return json.dumps({"errno": 1, "data": "请先前往首页登录登录http://ishabing.club"})
