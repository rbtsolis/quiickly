from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from apps.users.models import Quiickler
from apps.products.models import Product


'''

This is a Model of Orders

'''
class Order(models.Model):

    PAY_METHOD_CHOICES = (
        ('0', _('Tarjeta de Crédito')),
        ('1', _('Contrapedido')),
    )

    user          = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))
    address       = models.CharField(_('Dirección'), max_length=200)
    quiickler     = models.ForeignKey(Quiickler)
    product       = models.ForeignKey(Product, verbose_name=_('Producto'))
    latitude      = models.DecimalField(_('Latitud'), max_digits=20, decimal_places=5)
    longitude     = models.DecimalField(_('Longitud'), max_digits=20, decimal_places=5)
    pay_method    = models.CharField(_('Tipo de Pago'), choices=PAY_METHOD_CHOICES,max_length=25)
    unsolved      = models.BooleanField(_('Pendiente'), default=False)
    amount        = models.PositiveIntegerField(_('Monto'))
    complete      = models.BooleanField(_('Completado'), default=False)

    class Meta:

        db_table = 'orders'
