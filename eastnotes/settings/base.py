import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..")
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
SECRET_KEY = 'v8_ce#n3lleuhl(t4p^x)bd18_aarlmd$e!f*^4edjlm@*=9&)'
ROOT_URLCONF = 'eastnotes.urls'
WSGI_APPLICATION = 'eastnotes.wsgi.application'
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))  # 使apps目录优于其他目录被import语句检索到

# 文章列表分页数量
ARTICLE_PAGINATE_BY = 8

# 书单影单分页数量
BOOK_MOVIE_PAGINATE_BY = 8

# 搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7

# 中间件
MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

# APP注册
INSTALLED_APPS = [
    # 自己开发的APP
    'apps.blog',
    'apps.notice',
    'apps.setting',
    'apps.comment',
    'notifications',
    'apps.myzone',

    # 第三方插件
    'xadmin',
    'haystack',
    'mdeditor',
    'ckeditor',
    'crispy_forms',
    'rest_framework',

    # 系统内置
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CKEditor配置项
CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote','CodeSnippet'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,

        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', ]),
    },

    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}


# 使用whoosh搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 静态文件路径
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')

# 媒体资源路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 消息通知配置
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True
}

# 数据库编码配置
SILENCED_SYSTEM_CHECKS = ['mysql.E001']

# 配置缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379',
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#              "PASSWORD": "",
#         },
#     },
# }


