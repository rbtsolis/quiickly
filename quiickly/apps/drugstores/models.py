from django.db import models
from django.utils.translation import ugettext_lazy as _

'''

This is a Model of Drugstores

'''
class Drugstore(models.Model):

    name    = models.CharField(_('Nombre'), max_length=50)
    address = models.TextField(_('Dirección'))
    phone   = models.PositiveIntegerField(_('Teléfono'))
    city    = models.CharField(_('Ciudad'), max_length=50)
    email   = models.EmailField(_('Correo'))

    class Meta:

        db_table = 'drugstores'
