import xadmin
from .models import *


class CommentAdmin(object):
    list_display = ['id', 'object_id', 'text', 'comment_time', 'user']
    search_fields = ['content_type']
    model_icon = 'fa fa-comment'


xadmin.site.register(Comment, CommentAdmin)
