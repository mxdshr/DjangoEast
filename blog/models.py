# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField


# 创建博文分类的表
class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='分类名称')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="分类目录"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:category', kwargs={'pk': self.pk})


# 创建文章标签的表
class Tag(models.Model):
	# name是标签名的字段
	name = models.CharField(max_length=100, verbose_name='标签名称')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="标签列表"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:tag_list', kwargs={'pk': self.pk})


# 创建文章的类
class Post(models.Model):

	# 发表状态
	PUBLISH_STATUS = (
		('p', '已发表'),
		('d', '草稿箱'),
		('r', '回收站'),
	)

	# 是否置顶
	STICK_STATUS = (
		('y', '置顶'),
		('n', '不置顶'),
	)

	title = models.CharField('标题', max_length=100, unique=True)
	body = MDTextField('正文')
	created_time = models.DateTimeField('创建时间', default=timezone.now)
	modified_time = models.DateTimeField('修改时间', auto_now=True)
	excerpt = models.CharField('摘要', max_length=200, blank=True, )
	views = models.PositiveIntegerField('阅读量', default=0)
	words = models.PositiveIntegerField('字数', default=0)
	category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag, verbose_name='标签类型', blank=True)
	author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, default="reborn")
	status = models.CharField('文章状态', max_length=1, choices=PUBLISH_STATUS, default='p')
	stick = models.CharField('是否置顶', max_length=1, choices=STICK_STATUS, default='n')

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	def get_user(self):
		return self.author

	# 阅读量增加1
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.body).replace("&nbsp;","").replace("#","")[:150] #strip_tags是去除html标签
		self.words = len(strip_tags(self.body).replace(" ","").replace('\n',""))	# 统计文章字数
		super(Post, self).save(*args, **kwargs) # 调用父类的 save 方法将数据保存到数据库中

	class Meta:
		verbose_name = "文章列表"
		verbose_name_plural = verbose_name
		ordering = ['-created_time']


class BookCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="分类名称")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "图书分类"
		verbose_name_plural = verbose_name


class BookTag(models.Model):
	name = models.CharField(max_length=100, verbose_name="标签")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:book_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "书籍标签"
		verbose_name_plural = verbose_name


class Book(models.Model):
	name = models.CharField("书名", max_length=100)
	author = models.CharField("作者", max_length=100)
	category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name="书籍分类")
	tag = models.ManyToManyField(BookTag, verbose_name="本书标签")
	cover = models.ImageField("封面图", upload_to='books', blank=True)
	score = models.DecimalField("豆瓣评分", max_digits=2, decimal_places=1)
	created_time = models.DateField("添加时间", null=True, default=timezone.now)
	time_consuming = models.CharField("阅读初始时间", max_length=100)
	pid = models.CharField("文章ID", max_length=100, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pid})

	class Meta:
		verbose_name = "我的书单"
		verbose_name_plural = verbose_name


class MovieCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="电影分类")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="电影分类"
		verbose_name_plural = verbose_name


class MovieTag(models.Model):
	name = models.CharField(max_length=100,verbose_name="标签名称",blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:movie_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name="电影标签"
		verbose_name_plural=verbose_name


class Movie(models.Model):
	name = models.CharField("电影名称", max_length=100)
	director = models.CharField("导演", max_length=100)
	actor = models.CharField("主演", max_length=100)
	category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, verbose_name="电影分类")
	tag = models.ManyToManyField(MovieTag, verbose_name="电影标签")
	cover = models.ImageField("上传封面", upload_to='movies', blank=True)
	score = models.DecimalField("豆瓣评分", max_digits=2, decimal_places=1)
	release_time = models.DateField("上映时间")
	created_time = models.DateField("添加时间", default=timezone.now)
	length_time = models.PositiveIntegerField("电影时长", default=0)
	watch_time = models.DateField("观看时间", default=timezone.now)
	pid = models.CharField("文章ID", max_length=100, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pid})

	class Meta:
		verbose_name = "我的影单"
		verbose_name_plural = verbose_name


class Messages(models.Model):
	name = models.CharField(max_length=100,verbose_name="给我留言")
	admin = models.ForeignKey(User,verbose_name='站长',on_delete=models.CASCADE,blank=True,null=True)

	def get_absolute_url(self):
		return reverse('blog:messages')

	def get_user(self):
		return self.admin

	class Meta:
		verbose_name = "网站留言"
		verbose_name_plural = verbose_name


class MeanList(models.Model):
	title = models.CharField("菜单名称", max_length=100)
	link = models.CharField("菜单链接", max_length=100, blank=True,null=True,)
	icon = models.CharField("菜单图标", max_length=100, blank=True,null=True,)

	class Meta:
		verbose_name = "菜单栏"
		verbose_name_plural = verbose_name


class Courses(models.Model):
	title = models.CharField(max_length=100,verbose_name="教程名称")
	cover = models.ImageField(upload_to='course',verbose_name="上传封面",blank=True)
	views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
	category = models.CharField(max_length=100,verbose_name="教程分类")
	introduce = models.CharField(max_length=200,verbose_name="教程简介",blank=True)
	status = models.CharField(max_length=50,verbose_name="更新状态")
	created_time = models.DateTimeField(null=True, verbose_name='创建时间', default=timezone.now)
	author = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING, default="reborn")
	comments = models.PositiveIntegerField(default=0, verbose_name="评论数")
	numbers = models.PositiveIntegerField(default=0, verbose_name="教程数量")

	class Meta:
		verbose_name = "教程列表"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:course', kwargs={'pk': self.pk})