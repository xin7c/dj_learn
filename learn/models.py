# coding:utf-8
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=12)
    sex = models.CharField(max_length=2)
    age = models.IntegerField()

    def __unicode__(self):
        result = self.name + ":" + self.sex + ":" + str(self.age)
        print("查询model.User")
        return result