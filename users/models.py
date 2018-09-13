# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    mobile = models.CharField(max_length=11, verbose_name=u'电话号码')
    add_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
