from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class Customer(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.name