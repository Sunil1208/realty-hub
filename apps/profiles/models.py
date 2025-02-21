from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), blank=True, null=True, max_length=15
    )
    about = models.TextField(
        verbose_name=_("About me"), default="Say something about yourself"
    )
    license = models.CharField(
        verbose_name=_("Real Estate License"), max_length=20, blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER
    )
    country = CountryField(
        verbose_name=_("Country"), default="IN", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        default="Mumbai",
        max_length=180,
        blank=False,
        null=False,
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text=_("Are you looking to buy a property?"),
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"),
        default=False,
        help_text=_("Are you looking to sell a property?"),
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"),
        default=False,
        help_text=_("Are you a real estate agent?"),
    )
    top_agent = models.BooleanField(
        verbose_name=_("Top Agent"),
        default=False,
        help_text=_("Are you a top real estate agent?"),
    )
    rating = models.DecimalField(
        verbose_name=_("Rating"),
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    num_reviews = models.PositiveIntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
