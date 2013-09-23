# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from core.models import Score, SUser, BaseRate


class Executor(SUser, BaseRate):
    busy = models.BooleanField(_(u'Занят'), default=False)


class Customer(SUser, BaseRate):
    contacts = models.CharField(_(u'Контакты'), max_length=1024, blank=True)
