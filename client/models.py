# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from core.models import Score

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


class Executor(SUser):
    score = models.ForeignKey(Score, verbose_name=_(u'Счет исполнителя'))
    busy = models.BooleanField(_(u'Занят'), default=False)


class Customer(SUser):
    score = models.ForeignKey(Score, verbose_name=_(u'Счет заказчика'))
