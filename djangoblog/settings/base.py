import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..")
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
SECRET_KEY = 'v8_ce#n3lleuhl(t4p^x)bd18_aarlmd$e!f*^4edjlm@*=9&)'
ROOT_URLCONF = 'djangoblog.urls'
WSGI_APPLICATION = 'djangoblog.wsgi.application'
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r'http://code.jquery.com/jquery-2.1.1.min.js'}

# 文章列表分页数量
ARTICLE_PAGINATE_BY = 7

# 书单影单分页数量
BOOK_PAGINATE_BY = 8

# 搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# APP注册
INSTALLED_APPS = [
    'blog',
    'notice',
    'setting',
    'comment',
    'notifications',

    'xadmin',
    'crispy_forms',
    'haystack',
    'mdeditor',
    'ckeditor',
    'debug_toolbar',
    'rest_framework',

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

# Haystack搜索引擎框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
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
