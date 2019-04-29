from django.db import models
import django.utils.timezone as timezone

# 友情链接
class FriendLinks(models.Model):
    name = models.CharField(max_length=50,verbose_name="网站名称")
    link = models.URLField(max_length=200,verbose_name="网站地址")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['-pk']

# SEO设置
class Seo(models.Model):
    title = models.CharField(max_length=100,verbose_name="网站主名称")
    sub_title = models.CharField(null=True,blank=True,max_length=200,verbose_name="网站副名称")
    description = models.CharField(max_length=300,verbose_name="网站描述")
    keywords = models.CharField(max_length=200,verbose_name="关键字")

    class Meta:
        verbose_name = "SEO设置"
        verbose_name_plural = verbose_name

# 自定义代码
class CustomCode(models.Model):
    statistics = models.TextField(null=True,blank=True,verbose_name="网站统计代码")


    class Meta:
        verbose_name = "自定义代码"
        verbose_name_plural = verbose_name

# 站点信息
class SiteInfo(models.Model):
    created_time = models.DateField(null=True,blank=True,default = timezone.now,verbose_name="建站时间")
    record_info = models.CharField(null=True,blank=True,max_length=100,verbose_name="备案信息")
    development_info = models.CharField(null=True,blank=True,max_length=100,verbose_name="开发信息")
    arrange_info = models.CharField(null=True,blank=True,max_length=100,verbose_name="部署信息")

    class Meta:
        verbose_name = "站点信息"
        verbose_name_plural = verbose_name

# 社交账号
class Social(models.Model):
    github = models.URLField(null=True,blank=True,max_length=200,verbose_name="Github地址")
    wei_bo = models.URLField(null=True,blank=True,max_length=200,verbose_name="微博地址")
    zhi_hu = models.URLField(null=True,blank=True,max_length=200,verbose_name="知乎地址")
    qq = models.CharField(null=True,blank=True,max_length=20,verbose_name="QQ号码")
    wechat = models.CharField(null=True,blank=True,max_length=50,verbose_name="微信")
    official_wechat = models.CharField(null=True,blank=True,max_length=50,verbose_name="微信公众号")


    class Meta:
        verbose_name = "社交账号"
        verbose_name_plural = verbose_name
