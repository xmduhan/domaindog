# -*- coding: utf-8 -*-

from django.contrib import admin
from models import DomainTest
# Register your models here.



class DomainTestAdmin(admin.ModelAdmin):
    '''
    '''
    fields = ['domain', 'state']
    list_display = ['domain', 'state']
    list_filter = ['state']


admin.site.register(DomainTest, DomainTestAdmin)
