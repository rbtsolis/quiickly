from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from apps.users.models import Quiickler, Address, User
from apps.products.models import Product
from apps.orders.models import Order


'''

This is a Model of Drugstores

'''
class Drugstore(models.Model):

    name     = models.CharField(_('Nombre'), max_length=50)
    branches = models.ManyToManyField('BranchOffice', verbose_name=_('Sucursales'))
    user     = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))


    def __str__(self):
        return "%s" % (self.name)


    class Meta:

        db_table = 'drugstores'


'''
This is a Model of Branch Office(Sucursal)

'''
class BranchOffice(models.Model):

    name       = models.CharField(_('Nombre'), max_length=50)
    agent      = models.CharField(_('Representante'), max_length=50)
    phone      = models.PositiveIntegerField(_('Teléfono'))
    email      = models.EmailField(_('Correo'))
    city       = models.CharField(_('Ciudad'), max_length=50)
    is_smart   = models.BooleanField(_('Smartphone'), default=True)
    avaliable  = models.BooleanField(default=False)
    quiicklers = models.ManyToManyField(Quiickler)
    address    = models.ForeignKey(Address, verbose_name=_('Dirección'))
    schedule   = models.CharField(_('Horario'), max_length=50)
    products   = models.ManyToManyField(Product, verbose_name=_('Productos'))
    user       = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))
    orders     = models.ManyToManyField(Order, verbose_name=_('Pedidos'))

    def __str__(self):
        return "%s" % (self.name)

    class Meta:

        db_table = 'branch_offices'
