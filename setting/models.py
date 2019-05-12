from django.db import models
import django.utils.timezone as timezone


# 友情链接
class FriendLinks(models.Model):
    name = models.CharField('网站名称', max_length=50, default='向东的笔记本')
    link = models.CharField('网站地址', max_length=200, default='https://www.eastnotes.com')

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


# SEO设置
class Seo(models.Model):
    title = models.CharField("网站主名称", max_length=100, default='DjangoEast')
    sub_title = models.CharField("网站副名称", max_length=200, default='DjangoEast')
    description = models.CharField("网站描述", max_length=200, default='DjangoEast')
    keywords = models.CharField("关键字", max_length=200, default='DjangoEast')

    class Meta:
        verbose_name = "SEO设置"
        verbose_name_plural = verbose_name


# 自定义代码
class CustomCode(models.Model):
    statistics = models.TextField("网站统计代码", default='统计代码')

    class Meta:
        verbose_name = "自定义代码"
        verbose_name_plural = verbose_name


# 站点信息
class SiteInfo(models.Model):
    created_time = models.DateField("建站时间", default=timezone.now)
    record_info = models.CharField("备案信息", max_length=100, default='备案号')
    development_info = models.CharField("开发信息", max_length=100, default='开发信息')
    arrange_info = models.CharField("部署信息", max_length=100, default='部署信息')

    class Meta:
        verbose_name = "站点信息"
        verbose_name_plural = verbose_name


# 社交账号
class Social(models.Model):
    github = models.URLField("Github地址", max_length=200, default='https://github.com/mxdshr/DjangoEast')
    wei_bo = models.URLField("微博地址", max_length=200, default='https://weibo.com/')
    zhi_hu = models.URLField("知乎地址", max_length=200, default='https://www.zhihu.com/people/sylax8/')
    qq = models.CharField("QQ号码", max_length=20, default='783342105')
    wechat = models.CharField("微信",max_length=50,default='reborn0502')
    official_wechat = models.CharField("微信公众号", max_length=50, default='程序员向东')

    class Meta:
        verbose_name = "社交账号"
        verbose_name_plural = verbose_name
