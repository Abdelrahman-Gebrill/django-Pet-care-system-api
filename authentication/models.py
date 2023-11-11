from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
#this imports allow us to inherit the django User model and modify it.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
# A registry that stores the configuration of installed applications.
# It also keeps track of models, e.g. to provide reverse relations.
from django.apps import apps
#to has the user password
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
#Used to generate the access and the refresh token
from rest_framework_simplejwt.tokens import RefreshToken


class MyUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    firstname = models.CharField(_('first name'), max_length=150,blank=False,null=False,)
    lastname = models.CharField(_('last name'), max_length=150,blank=False,null=False,)
    email = models.EmailField(_('email address'),unique=True,blank=False,null=False,)
    phoneNumber = models.CharField(
        _('phone number'),
        max_length=11,
        validators=[MinLengthValidator(limit_value=11,message='Phone Number must be 11 number'),RegexValidator(regex=r'01[1,2,5,0]{1}[0-9]{8}',message="must be valid Egyption Number")],
        unique=True,
    error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    blank=False,
    null=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    #used to generate token when call it
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access':str(refresh.access_token),
        }
    def __str__(self):
        return str(self.id)