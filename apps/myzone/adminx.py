import xadmin
from .models import *


class TalkTagsAdmin(object):
    list_display = ['id', 'name']
    model_icon = 'fa fa-tag'


class TalkContentAdmin(object):
    list_display = ['id', 'body', 'created_time', 'tag', 'status']
    model_icon = 'fa fa-file-text'


xadmin.site.register(TalkTags, TalkTagsAdmin)
xadmin.site.register(TalkContent, TalkContentAdmin)


