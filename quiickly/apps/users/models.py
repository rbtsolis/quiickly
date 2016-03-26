from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff,
                is_superuser, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(username = username, email=email, is_active=True,
                is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save( using = self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    id          = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    username    = models.CharField(max_length=100, unique=True)
    email       = models.EmailField(unique=True, blank=False, null=False)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    gender      = models.CharField(choices=gender_choices, max_length=50)
    avatar      = models.URLField()
    verify_code = models.CharField(max_length=512, blank=True, null=True, editable=False)
    created_on  = models.DateTimeField(auto_now_add=True)
    courses     = models.ManyToManyField('courses.Course', blank=True)
    slug        = models.SlugField(editable=False, db_column='slug')

    objects = UserManager()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','email','gender']

    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.username.replace(".","-"))
            super(User, self).save(*args, **kwargs)
        else:
            super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.username

    def full_name(self):
        return title('%s %s' % (self.first_name, self.last_name))

    class Meta:

        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')


'''
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
'''


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255, unique=True,
                              db_index=True,)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


@python_2_unicode_compatible
class AbstractNamedUser(AbstractEmailUser):
    name = models.CharField(_('name'), max_length=255)

    REQUIRED_FIELDS = ['name']

    class Meta:
        abstract = True
        ordering = ['name', 'email']

    def __str__(self):
        return '{name} <{email}>'.format(
            name=self.name,
            email=self.email,
        )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name


class TimeStampedModel(models.Model):
    """ TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractNamedUser):

    class Meta(AbstractNamedUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')

