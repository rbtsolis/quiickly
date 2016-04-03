from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff,
                is_superuser, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True,
                is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save( using = self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False,
                False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True,
                True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id          = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    username    = models.CharField(max_length=100, unique=True)
    email       = models.EmailField(_('Correo'), unique=True, blank=False, null=False)
    name        = models.CharField(_('Nombre'), max_length=100)
    avatar      = models.URLField(_('Avatar'))
    phone       = models.PositiveIntegerField(_('Teléfono'))
    address     = models.ManyToManyField('Address')

    verify_code = models.CharField(max_length=512, blank=True, null=True, editable=False)
    date_joined = models.DateTimeField(_('Fecha de Ingreso'), auto_now_add=True)
    modified    = models.DateTimeField(_('Fecha Modificado'), auto_now=True)

    objects = UserManager()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'avatar', 'phone']


    def __str__(self):
        return "%s" % (self.name)

    def get_short_name(self):
        return '%s' % (self.name)

    def full_name(self):
        return '%s' % (self.name)

    def save(self, *args, **kwargs):

        if not self.username:
            self.username = self.email
            super(User, self).save(*args, **kwargs)
        else:
            super(User, self).save(*args, **kwargs)

    class Meta:

        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Address(models.Model):

    address   = models.TextField(_('Dirección'))
    latitude  = models.DecimalField(_('Latitud'), max_digits=20, decimal_places=5)
    longitude = models.DecimalField(_('Longitud'), max_digits=20, decimal_places=5)

    class Meta:
        db_table = 'address'


class Quiickler(models.Model):

    user          = models.ForeignKey('User')
    license_plate = models.CharField(_('Placa'), max_length=50)

    class Meta:

        db_table = 'quiicklers'
