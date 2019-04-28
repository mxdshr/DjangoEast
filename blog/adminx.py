#-*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

# 此类可以定义admin后台显示的字段，比如文章列表显示标题，创建时间，
class PostAdmin(object):
    # 展示的字段
    list_display = ['id','title','created_time','category']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id','title','created_time','category']
    # 修改图标
    model_icon = 'fa fa-bell'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['']

    list_display_link = ['title']

    # style_fields = {'body':'ueditor'}

class CategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-briefcase'

class TagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-tags'

# 图书分类
class BookCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'

# 图书
class BookAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'

# 图书标签
class BookTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-book'

# 电影分类
class MovieCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'

# 电影
class MovieAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'

# 电影标签
class MovieTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-film'

class MeanListAdmin(object):
    list_display = ['id','title','link','icon']
    search_field = ['title']
    model_icon = 'fa fa-list'

class CoursesAdmin(object):
    list_display = ['id','title','views','category','created_time','comments','numbers']
    model_icon = 'fa fa-gift'

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)

xadmin.site.register(BookCategory,BookCategoryAdmin)
xadmin.site.register(Book,BookAdmin)
xadmin.site.register(BookTag,BookTagAdmin)

xadmin.site.register(MovieCategory,MovieCategoryAdmin)
xadmin.site.register(Movie,MovieAdmin)
xadmin.site.register(MovieTag,MovieTagAdmin)

xadmin.site.register(MeanList,MeanListAdmin)

xadmin.site.register(Courses,CoursesAdmin)
# 修改xadmin的基础配置
class BaseSetting(object):
    # 允许使用主题
    enable_themes = True
    use_bootswatch = True

# 修改xadmin的全局配置
class GlobalSetting(object):
    site_title = '向东的笔记本'
    site_footer = '2019'

    # Models收起功能
    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )