from django.db import models

# Create your models here.
class LY(models.Model):
    data=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    userid=models.CharField(max_length=1000)
class USER(models.Model):
    name=models.CharField(max_length=100)
    msg=models.CharField(max_length=1000)
class WZ(models.Model):
    # 标题



    wz_name=models.CharField(max_length=500)
    # 作者寄语
    wz_zzjy=models.CharField(max_length=1000)
    # 内容
    wz_nr=models.TextField(max_length=10000)
    # 时间
    wz_time=models.CharField(max_length=20)
    # 作者
    wz_zz=models.CharField(max_length=20)
    # 点赞
    wz_dz=models.IntegerField()
    # 浏览量
    wz_lll=models.IntegerField()
    # 备用
    wz_by1 = models.CharField(max_length=1000)
    # 备用
    wz_by2 = models.CharField(max_length=1000)
class PL(models.Model):
    pl_id=models.IntegerField
    pl_zt=models.CharField(max_length=200)
    pl_bt=models.CharField(max_length=200)
    pl_name=models.CharField(max_length=200)
    con=models.CharField(max_length=10000)
    pl_time=models.CharField(max_length=20)