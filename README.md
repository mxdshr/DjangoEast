# DjangoEast

本网站基于`Django2.1`和`Python3.6`开发完成，前端样式由`Bootstrap`驱动，支持响应式布局，支持多种终端显示。

[![Build Status](https://travis-ci.org/mxdshr/DjangoEast.svg?branch=master)](https://travis-ci.org/mxdshr/DjangoEast) ![GitHub release](https://img.shields.io/github/release/mxdshr/DjangoEast.svg)  [![Requirements Status](https://requires.io/github/mxdshr/DjangoEast/requirements.svg?branch=master)](https://requires.io/github/mxdshr/DjangoEast/requirements/?branch=master) ![GitHub](https://img.shields.io/github/license/mxdshr/DjangoEast.svg)

## 1. 主要功能
- 支持访客留言功能
- 支持登录和注册功能
- 文章可按日期、分类、标签等多种形式展示
- 网站后台使用xadmin，弥补了原生后台难看的缺点
- 文章底部支持多级评论，评论框支持富文本、`Markdown`
- 文章撰写支持`Markdown`编辑器，文章页展示支持代码高亮
- 支持登录用户消息提醒功能，有新文章评论第一时间得到通知
- 支持添加书单、影单功能，很适合喜欢读书，喜欢看电影的朋友
- 支持全站关键词搜索，搜索范围是文章标、内容，搜索结果关键词高亮显示
- 更多功能，敬请期待......

## 2. 本地安装
### 2.1 下载网站到本地
```bash
git clone https://github.com/mxdshr/DjangoEast.git
```
### 2.2 安装运行环境
```bash
pip install -r requirements.txt
```
### 2.3 修改配置文件
打开 `django/settins/local.py`文件，找到下面的代码，填写数据库信息
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名',
        'USER':'数据库账户名',
        'PASSWORD':'数据库账户密码',
        'PORT':'3306',
        'HOST':'localhost',
    }
}
```
### 2.4 数据库迁移
网站根目录下终端执行
```bash
python manage.py makemigrations
python manage.py migrate
```
### 2.5 运行测试
网站根目录下终端执行
```bash
python manage.py runserver 127.0.0.1:8000
```
## 3. 线上部署
请参考：[(超详细)Django线上部署教程：腾讯云+Ubuntu+Django+Uwsgi](https://www.eastnotes.com/post/29)

## 4.问题交流
我建了一个`Django`建站交流群，此群主要讨论与`Django`建站相关的问题。如果你在学习`Django`时或者在使用`DjangoEast`中遇到了任何问题，都可以在群里进行交流，我会给大家进行解答。我还会不定期在群里分享有关Django学习的资料，包括电子书，视频教程等。

如果你想学习`Django`建站，可以加我微信：`reborn0502`，备注`Django`，我拉你进群。
## 4.更新日志

##第二版
### V2.1

- 文章支持放入回收站、草稿箱功能，被放入的文章不会再前端显示
- 文章分类、标签按所含文章数量倒序排列，且限制显示数量，增加查看更多超链接
- 优化菜单栏功能，可在后台选择显示与隐藏菜单条目
- 添加我的说说功能，可在后台发表想法
- 优化归档页展示效果，文章按月份折叠展示

### V2.0
2019.5.7，第二个版本，新增了很多功能，前端样式大改版，功能日渐完善，具体如下：
- 新增我的书单、我的影单功能，读书和电影爱好者的福利
- 支持登录、注册功能，注册后可进行文章评论
- 新增文章评论功能，评论框支持富文本， 由`Ckeditor`编辑器驱动，评论区支持二级显示
- 新增网站留言功能，是文章评论功能的拓展
- 前端改用`Bootstrap`框架，再也不用调CSS样式调到恶心想吐了
- 登录用户可在导航栏查看评论消息通知，由`django-notifications-hq`驱动
- 后台支持网站信息设置，包括标题，关键字、描述等

##第一版
### V1.0
2019.3.7，由`Django2.0`和`Python3.6`开发的个人博客网站首次上线，使用`Nginx+Gunicorn`部署于腾讯云服务器，功能尚且简陋，具体如下：
- 前端模板仿制`Next`主题，后台管理替换为`Xadmin`
- 支持文章按分类、标签、日期展示
- 支持全站文章搜索，由`Whoosh+Haystack+Jieba`3个库联合驱动，搜索内容限文章标题、文章内容
- 文章添加和展示同时支持`Markdown`语法，由`Markdown+Mdeditor`2个库联合驱动
- 文章内容中代码块支持`语法高亮`，由`Pygments`库驱动