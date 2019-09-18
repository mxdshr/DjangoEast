from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone


class TalkTags(models.Model):
    name = models.CharField("说说标签", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "说说标签"
        verbose_name_plural = verbose_name
        ordering = ['id']


class TalkContent(models.Model):

    STATUS = (
        ('y', "公开"),
        ('n', '私密')
    )

    body = MDTextField('说说正文')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    tag = models.ManyToManyField(TalkTags, verbose_name="说说标签")
    status = models.TextField("发表状态", choices=STATUS, default='y')

    class Meta:
        verbose_name = "说说内容"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
