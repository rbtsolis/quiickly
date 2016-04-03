from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import Quiickler, Address


'''

This is a Model of Drugstores

'''
class Drugstore(models.Model):

    name     = models.CharField(_('Nombre'), max_length=50)
    branches = models.ManyToManyField('BranchOffice', verbose_name=_('Sucursales'))

    class Meta:

        db_table = 'drugstores'


'''
This is a Model of Branch Office(Sucursal)

'''
class BranchOffice(models.Model):

    agent      = models.CharField(_('Representante'), max_length=50)
    phone      = models.PositiveIntegerField(_('Teléfono'))
    email      = models.EmailField(_('Correo'))
    city       = models.CharField(_('Ciudad'), max_length=50)
    is_smart   = models.BooleanField(_('Smartphone'), default=True)
    avaliable  = models.BooleanField(default=False)
    quiicklers = models.ManyToManyField(Quiickler)
    address    = models.ForeignKey(Address)
