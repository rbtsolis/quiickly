# -*- coding:utf-8 -*-

from django.db import models
#from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


from apps.users.models import User, Quiickler


DISTRIBUTION = (
    ('0', _('Aplicacion')),
    ('1', _('Web')),
    ('2', _('Web y App'))
)

STATE = (
    ('1', _('Disponible')),
    ('0', _('Agotado')),
)


"""

Model to manage brands of condoms

"""
class Brand(models.Model):

    name      = models.CharField(_("Marca"), max_length=50)
    created   = models.DateTimeField(_("Creado"), auto_now_add=True)
    modified  = models.DateTimeField(_("Modificado"), auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'brands'
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


"""

Model Product, this is a condom

"""
class Product(models.Model):

    name        = models.CharField(_('Nombre'), max_length=50)
    description = models.TextField(_("Descripción"), null=True, blank=True)
    brand       = models.ForeignKey('Brand', related_name='brands')
    type        = models.ForeignKey('Type', related_name='types')
    stock       = models.PositiveIntegerField()
    state       = models.CharField(_("Estado"), max_length=15, choices=STATE)

    distribution = models.CharField(
        _("Canal de distribucion"),
        max_length=15,
        choices=DISTRIBUTION,
        default='app'
    )

    price            = models.FloatField(_("Precio express"))
    price_programing = models.FloatField(_("Precio Programado"), null=True)
    image            = models.ImageField(_("Imagen"), upload_to='img_producto/')
    image_ondemand   = models.ImageField(
        _("Imagen Ondemand"),
        upload_to ='img_producto/',
        null=True,
        blank=True
    )
    created   = models.DateTimeField(_("Creado"), auto_now_add=True)
    modified  = models.DateTimeField(_("Modificado"), auto_now=True)

    def __str__(self):
        return "%s"%(self.name)

    def save(self, *args, **kwargs):

        print(self.state)
        if self.stock <= 0 and self.state == 1:
            self.state = 0
            super(Product, self).save(*args, **kwargs)
        else:
            self.state = 1
            super(Product, self).save(*args, **kwargs)


    def total(self):
        return self.price * self.stock

    class Meta:
        db_table = 'products'


@receiver(pre_save, sender=Product)
def model_pre_save(sender, instance, **kwargs):

    stock_product = instance.stock
    if stock_product == 0:
        instance.state = 0


'''

Model to manage types of condoms

'''
class Type(models.Model):

    type      = models.CharField("Tipo", max_length=50)
    created   = models.DateTimeField(_("Creado"), auto_now_add=True)
    modified  = models.DateTimeField(_("Modificado"), auto_now=True)

    def __str__(self):
        return '%s' % self.type

    class Meta:

        db_table = 'types_products'
