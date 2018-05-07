from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext as _


class UserRole(object):
    EDITOR = 'editor'
    WRITER = 'writer'

    CHOICES = (
        (EDITOR, 'Editor'),
        (WRITER, 'Writer'),
    )


class Gender(object):
    MALE = 'male'
    FEMALE = 'female'

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )


class UserManager(BaseUserManager):
    """
    User model manager.
    """

    def create_user(self, username, first_name, last_name, gender, role, password):
        """
        Creates and saves a User with the given parameters.
        """
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            role=role,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, first_name, last_name, gender, role, password):
        """
        Creates and saves a Superuser with the given parameters.
        """
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            role=role,
        )
        user.is_active = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model.
    """
    username = models.CharField(verbose_name='user name', max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_('first name'), max_length=255)
    last_name = models.CharField(verbose_name=_('last name'), max_length=255)
    gender = models.CharField(max_length=50, choices=Gender.CHOICES)
    role = models.CharField(max_length=50, choices=UserRole.CHOICES)

    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(
        verbose_name=_('admin status'),
        default=False,
        help_text=_('Designates whether the user can log into this Django Admin Site.'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        """
        Returns the first_name and the last_name, with a space in between.
        """
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    @property
    def short_name(self):
        """
        Returns first name.
        """
        return self.first_name

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        Simplest possible answer: All admins are staff
        """
        return self.is_superuser
