from django.db import models
from django.utils.translation import ugettext_lazy as _
from custom_user.models import AbstractEmailUser, EmailUserManager


class User(AbstractEmailUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    image = models.ImageField(upload_to='ui', null=True, blank=True)
    about = models.TextField(max_length=1023, null=True, blank=True)

    objects = EmailUserManager()

    def __unicode__(self):
        if self.username:
            return self.username
        elif self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return ""
