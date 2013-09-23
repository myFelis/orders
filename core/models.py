# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext as _


class BaseState(models.Model):
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta(object):
        abstract = True

    def is_active(self):
        return self.active

    def is_deleted(self):
        return self.deleted


class Score(models.Model):
    debit = models.PositiveIntegerField(_(u'Приход'), default=0)
    credit = models.PositiveIntegerField(_(u'Расход'), default=0)
    transfer = models.ForeignKey('self', verbose_name=_(u'Переведено со счета'),
        blank=True, related_name='transfer_score')

    def __unicode__(self):
        return "%s / %s" % (self.debit, self.credit)
