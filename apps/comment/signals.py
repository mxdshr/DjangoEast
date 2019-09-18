from django.db.models.signals import post_save
from notifications.signals import notify
from django.utils.html import strip_tags
from .models import Comment
from django.dispatch import receiver

# @receiver(post_save,sender=Comment)
# def send_notification(sender,instance,**kwargs):
#     # 发送站内通知
#     # 判断评论的是博客还是
#     if instance.reply_to is None:
#         # 接受者是文章
#         recipient = instance.content_object.get_user()
#         if instance.content_type.model == 'post':
#             blog = instance.content_object
#             verb = '{0} 评论了你的文章：《{1}》'.format(instance.user, blog.title)
#         else:
#             raise Exception('不明评论')
#
#     else:
#         # 接受者是作者
#         recipient = instance.reply_to
#         verb = '{0} 评论了你的评论：{1}'.format(instance.user, strip_tags(instance.parent.text))
#     url = instance.content_object.get_absolute_url() + '#comment_'+str(instance.pk)
#
#     notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance,url=url)


@receiver(post_save, sender=Comment)
def send_notification(sender, instance, **kwargs):
    # 发送站内通知
    # 判断评论的是博客还是
    if instance.reply_to is None:
        # 接受者是文章
        recipient = instance.content_object.get_user()
        if instance.content_type.model == 'post':
            blog = instance.content_object
            verb = '{0} 评论了你的文章：《{1}》'.format(instance.user, blog.title)
        elif instance.content_type.model == 'messages':
            verb = '{0} 给你留言'.format(instance.user)
        else:
            raise Exception('unknown messages')
    else:
        # 接受者是作者
        recipient = instance.reply_to
        verb = '{0} 评论了你的评论：{1}'.format(instance.user, strip_tags(instance.parent.text))
    url = instance.content_object.get_absolute_url() + '#comment_'+str(instance.pk)

    notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance,url=url)