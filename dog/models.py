# -*- coding: utf-8 -*-

from django.db import models

#Create your models here.




class DomainTest(models.Model):
    '''
    域名测试记录
    '''
    STATE = (('unknown', u'未知'), ('used', u'在使用'),('free', u'未使用'),('error',u'出错'))
    domain = models.CharField(u'域名', max_length=256)
    state = models.CharField(u'状态', max_length=20, choices=STATE)
