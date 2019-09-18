from django.apps import AppConfig


class CommentConfig(AppConfig):
    name = 'apps.comment'
    verbose_name = '评论管理'

    def ready(self):
        super(CommentConfig,self).ready()
        from . import signals
