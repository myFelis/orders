# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

def normalize_email(username):
    try:
        email_name, domain_name = username.strip().split('@', 1)
    except ValueError:
        return False
    else:
        username = '@'.join([email_name.lower(), domain_name.lower()])
    return username


class SUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **kwargs):
        email = normalize_email(email)
        if not email:
            raise ValueError('We need an email to create a new user')
        user = self.model(email=email, **kwargs)
        password = password if password else 'test'
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class SUser(AbstractBaseUser):
    email = models.EmailField(_(u"Email"), max_length=255, db_index=True, unique=True)
    username = models.CharField(_(u'Логин'), max_length=32, blank=True)

    objects = SUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _(u'Пользователь системы')
        verbose_name_plural = _(u'Пользователи системы')

    def __unicode__(self):
        return self.email


class BaseState(models.Model):
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta(object):
        abstract = True

    def is_active(self):
        return self.active

    def is_deleted(self):
        return self.deleted


class BaseRate(models.Model):
    rate = models.IntegerField(_(u'Рейтинг'), default=0)

    class Meta(object):
        abstract = True

    def is_active(self):
        return self.active

    def is_deleted(self):
        return self.deleted


class Score(models.Model):
    debit = models.PositiveIntegerField(_(u'Приход'), default=0)
    credit = models.PositiveIntegerField(_(u'Расход'), default=0)
    transfer = models.ForeignKey('self', null=True, blank=True,
        verbose_name=_(u'Переведено со счета'), related_name='transfer_score')
    user = models.OneToOneField(SUser, null=True, blank=True, verbose_name=_(u'Владелец'))

    def __unicode__(self):
        return "%s: %s / %s" % (self.user, self.debit, self.credit)
