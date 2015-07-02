# -*- coding: utf-8 -*-

"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS
:copyright: Copyriht (c) 2013-2014, deipi.com LLC. All
:license: See LICENSE for license details

"""

from __future__ import absolute_import, unicode_literals

from django.db import models


class SmsManager(models.Manager):
    pass


class BaseMessageModel(models.Model):
    text = models.TextField()
    total_parts = models.PositiveSmallIntegerField()
    quantity_parts = models.PositiveSmallIntegerField()
    date = models.TextField()

    delivered = models.ManyToManyField('Endpoint')

    class Meta:
        abstract = True

class SmsModel(BaseMessageModel):
    ref = models.PositiveIntegerField()
    phone = models.BigIntegerField()


class EmailModel(BaseMessageModel):
    email = models.EmailField()


class TextModel(BaseMessageModel):
    pass

class Endpoint(models.Model):
    url = models.CharField(max_length=100)

            