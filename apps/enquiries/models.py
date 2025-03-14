from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Your Name"), max_length=255)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), blank=True, max_length=15
    )
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(verbose_name=_("Subject"), max_length=128)
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Enquiry")
        verbose_name_plural = _("Enquiries")
