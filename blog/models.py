# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField
# 创建博文分类的表
class Category(models.Model):
	name = models.CharField(max_length=100,verbose_name='分类名称')

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
	name = models.CharField(max_length=100,verbose_name='标签名称')
	def __str__(self):
		return self.name

	class Meta:
		verbose_name="标签列表"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:tag_list', kwargs={'pk': self.pk})


# 创建文章的类
class Post(models.Model):

	title = models.CharField(max_length=1000,verbose_name='标题')
	body = MDTextField(verbose_name='正文')
	created_time = models.DateTimeField(null=True,verbose_name='创建时间',default = timezone.now)
	modified_time = models.DateTimeField(verbose_name='修改时间',auto_now = True)
	excerpt = models.CharField(max_length=300,blank=True,verbose_name='摘要')
	views = models.PositiveIntegerField(default=0)
	words = models.PositiveIntegerField(default=0)
	category = models.ForeignKey(Category,verbose_name='文章分类',on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag,verbose_name='标签类型')
	author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE,default="reborn")

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
		verbose_name="文章列表"
		verbose_name_plural = verbose_name
		ordering= ['-pk']

class BookCategory(models.Model):
	name = models.CharField(max_length=100,verbose_name="分类名称")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "图书分类"
		verbose_name_plural = verbose_name

class BookTag(models.Model):
	name = models.CharField(max_length=100,verbose_name="标签")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:book_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "书籍标签"
		verbose_name_plural = verbose_name


class Book(models.Model):
	name = models.CharField(max_length=100,verbose_name="书名")
	author = models.CharField(max_length=100, verbose_name="作者")
	category = models.ForeignKey(BookCategory,on_delete=models.CASCADE,verbose_name="书籍分类")
	tag = models.ManyToManyField(BookTag,verbose_name="本书标签")
	cover = models.ImageField(upload_to='books',verbose_name="封面图",blank=True)
	score = models.DecimalField(max_digits=2,decimal_places=1,verbose_name="豆瓣评分")
	title = models.CharField(max_length=100, verbose_name="标题",blank=True)
	detail = MDTextField(verbose_name="读书笔记", null=True,blank=True)
	created_time = models.DateField(null=True,default = timezone.now,verbose_name="添加时间")
	time_consuming = models.CharField(max_length=100,verbose_name="阅读初始时间")
	views = models.PositiveIntegerField(default=0,verbose_name="阅读量")
	words = models.PositiveIntegerField(default=0,verbose_name="字数")
	excerpt = models.CharField(max_length=300, blank=True, verbose_name='摘要')


	def get_absolute_url(self):
		return reverse('blog:book_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name

	# 阅读量增加1
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.detail).replace("&nbsp;","").replace("#","")[:150] #strip_tags是去除html标签
		self.words = len(strip_tags(self.detail).replace(" ","").replace('\n',""))	# 统计文章字数
		super(Book, self).save(*args, **kwargs) # 调用父类的 save 方法将数据保存到数据库中

	class Meta:
		verbose_name="我的书单"
		verbose_name_plural = verbose_name


class MovieCategory(models.Model):
	name = models.CharField(max_length=100,verbose_name="电影分类")

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
		return reverse('blog:movie_list',kwargs={'pk':self.pk})

	class Meta:
		verbose_name="电影标签"
		verbose_name_plural=verbose_name

class Movie(models.Model):
	name = models.CharField(max_length=100,verbose_name="电影名称")
	director = models.CharField(max_length=100,verbose_name="导演")
	actor = models.CharField(max_length=100,verbose_name="主演")
	category = models.ForeignKey(MovieCategory,on_delete=models.CASCADE,verbose_name="电影分类",)
	tag = models.ManyToManyField(MovieTag,verbose_name="电影标签")
	cover = models.ImageField(upload_to='movies',verbose_name="上传封面",blank=True)
	score = models.DecimalField(max_digits=2,decimal_places=1,verbose_name="豆瓣评分")
	release_time = models.DateField(verbose_name="上映时间")
	created_time = models.DateField(default=timezone.now,verbose_name="添加时间")
	length_time = models.PositiveIntegerField(default=0,verbose_name="电影时长")
	watch_time = models.DateField(default=timezone.now,verbose_name="观看时间")
	title = models.CharField(max_length=100,verbose_name="标题",blank=True)
	detail = MDTextField(blank=True,null=True,verbose_name="观影后感")
	views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
	words = models.PositiveIntegerField(default=0, verbose_name="字数")
	excerpt = models.CharField(max_length=300, blank=True, verbose_name='摘要')

	def __str__(self):
		return self.name

	# 阅读量增加1
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.detail).replace("&nbsp;","").replace("#","")[:150] #strip_tags是去除html标签
		self.words = len(strip_tags(self.detail).replace(" ","").replace('\n',""))	# 统计文章字数
		super(Movie, self).save(*args, **kwargs) # 调用父类的 save 方法将数据保存到数据库中

	def get_absolute_url(self):
		return reverse('blog:movie_detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name="我的影单"
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
	title = models.CharField(max_length=100,verbose_name="菜单名称")
	link = models.CharField(max_length=100,verbose_name="菜单链接",blank=True,null=True,)
	icon = models.CharField(max_length=100,verbose_name="菜单图标",blank=True,null=True,)

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