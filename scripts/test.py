#!/usr/bin/env python
# encoding: utf-8

from time import sleep
from dog.models import DomainTest
import pythonwhois




def run():
    while True:
        try:
            querySet = DomainTest.objects.filter(state='unknown')
            for i in querySet:
                result = pythonwhois.get_whois(i.domain)
                c1 = result['contacts']['admin'] == None
                c2 = len(result.keys())<5
                c3 = 'registrar' not in result
                if c1 and c2 and c3:
                    i.state = 'free'
                else:
                    i.state = 'used'
                i.save()
                sleep(1)
            return
        except Exception as e:
            print e
            i.state = 'error'
            i.save()
            sleep(5)
