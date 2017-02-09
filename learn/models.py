# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class User(models.Model):
    name = models.CharField(max_length=12)
    sex = models.CharField(max_length=2)
    age = models.IntegerField()

    def __unicode__(self):
        result = self.name + ":" + self.sex + ":" + str(self.age)
        print("查询model.User")
        return result

#python_2_unicode_compatible 会自动做一些处理去适应python不同的版本
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    # def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
    #     return self.title
    def __str__(self):
        return self.title