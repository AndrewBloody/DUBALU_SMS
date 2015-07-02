# -*- coding: utf-8 -*-

"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS
:copyright: Copyriht (c) 2013-2014, deipi.com LLC. All
:license: See LICENSE for license details

"""

from __future__ import absolute_import, unicode_literals
import urllib

from django.conf import settings
from django.views.generic import CreateView, ListView, View
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.db.models import F,Q
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import SmsModel, TextModel
from .forms import MySampleForm
from django.db.models import F,Q
from .tasks import test
from dehydration import dehydrate


class SmsEndpointsMixin(object):
    def dispatch_to_endpoints(self, sms):
        print 'Good Method dispatch'
        # crear una tarea de celery por cada ENDPOINT (enviar lista de objetos a enviar)
        test.apply_async(args=(dehydrate(sms),), kwargs=dict(local_settings=dehydrate(settings.load())))  # FIXME: branch should be sent dehydrated, but it fails at the moment
        

class ItemListView(ListView, SmsEndpointsMixin):
    model = SmsModel
    template_name = 'smsapp/item_list.html'
    
    def get_queryset(self):
        # Do query with manytomany to endpoint
        '''return self.model.objects.filter(
                Q(dirty=True) & (
                    Q(total_parts=F('quantity_parts')) #|
                #Q(date__gt=timezone.now() - datetime.timedelta(seconds=10))
                    )
                )
        '''
        SmsEndpointsMixin.dispatch_to_endpoints(self, 'HI')
        #self.model.objects.filter(delivered__url="http://127.0.0.1")
        return self.model.objects.filter()
        
    #@csrf_exempt   
    def post(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        #qs = self.get_queryset()

        # Catch crontab (sms)
        if self.request.body == 'sms':
            print 'SMS'
            SmsEndpointsMixin.dispatch_to_endpoints(self, 'HI')

        # Catch form

        # identificar fuente (sms, email)

        # filtrar mensajes que no han sido entregados por cada ENDPOINT

        #dispatch_to_endpoints()
        
        '''txt = ''
        for t in qs:
            #SAVE: concatenate field text
            txt += t.text + '|'

        for q in qs:
            if q.dirty == False:
                #TODO: update values
                qs.update(dirty=True)
        '''
        #return HttpResponseRedirect(reverse('item-list'))
        return HttpResponse('Just hi')

item_list = csrf_exempt(ItemListView.as_view())

class ItemCreateView(CreateView, SmsEndpointsMixin):
    model = TextModel
    form_class = MySampleForm
    template_name = 'smsapp/item_create.html'
    success_url = urlresolvers.reverse_lazy('item-list')

    def form_valid(self, form):
        ret = super(ItemCreateView, self)
        # Send ret to dispatch
        SmsEndpointsMixin.dispatch_to_endpoints(self)
        return ret
        
item_create = ItemCreateView.as_view()