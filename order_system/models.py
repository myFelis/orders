# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from client.models import Customer, Executor
from core.models import Score, BaseState


class System(BaseState):
    commission = models.PositiveIntegerField(_(u'Комиссия'), default=0)
    score = models.ForeignKey(Score, verbose_name=_(u'Счет'))

    def __unicode__(self):
        return _(u'Система')


class Order(BaseState):
    price = models.PositiveIntegerField(_(u'Цена'), default=0)
    customer = models.ForeignKey(Customer, verbose_name=_(u'Заказчик'))
    executor = models.ForeignKey(Executor, verbose_name=_(u'Исполнитель'))
    description = models.TextField(_(u'Описание'), max_length=4064, blank=True)
    title = models.TextField(_(u'Наименование'), max_length=512, default=' ')
    start = models.DateTimeField(_(u'Дата и время начала'), default=timezone.now)
    finish = models.DateTimeField(_(u'Дата и время завершения'), blank=True)

    def __unicode__(self):
        return self.title
