# Generated by Django 5.1.6 on 2025-03-01 11:48

import uuid

import autoslug.fields
import django.core.validators
import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                (
                    "ref_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        unique=True,
                        verbose_name="Property Reference Code",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default="Default description... update me please",
                        verbose_name="Description",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="IN", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Mumbai", max_length=180, verbose_name="City"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        default="795001",
                        max_length=20,
                        verbose_name="Postal Code",
                    ),
                ),
                (
                    "street_address",
                    models.CharField(
                        blank=True,
                        default="Gandhi Avenue",
                        max_length=255,
                        verbose_name="Street Address",
                    ),
                ),
                (
                    "property_number",
                    models.IntegerField(
                        default=112,
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Property Number",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Price",
                    ),
                ),
                (
                    "tax",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.15,
                        help_text="15% property tax charged",
                        max_digits=6,
                        verbose_name="Property Tax",
                    ),
                ),
                (
                    "plot_area",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Plot Area(m^2)",
                    ),
                ),
                (
                    "total_floors",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Number of floors"
                    ),
                ),
                (
                    "bedrooms",
                    models.PositiveIntegerField(default=1, verbose_name="Bedrooms"),
                ),
                (
                    "bathrooms",
                    models.DecimalField(
                        decimal_places=2,
                        default=1.0,
                        max_digits=4,
                        verbose_name="Bathrooms",
                    ),
                ),
                (
                    "advert_type",
                    models.CharField(
                        choices=[
                            ("For Sale", "For Sale"),
                            ("For Rent", "For Rent"),
                            ("Auction", "Auction"),
                        ],
                        default="For Sale",
                        max_length=50,
                        verbose_name="Advert Type",
                    ),
                ),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Apartment", "Apartment"),
                            ("House", "House"),
                            ("Office", "Office"),
                            ("Warehouse", "Warehouse"),
                            ("Commercial", "Commercial"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=50,
                        verbose_name="Property Type",
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True,
                        default="/house_sample.jpg",
                        null=True,
                        upload_to="",
                        verbose_name="Cover Photo",
                    ),
                ),
                (
                    "photo1",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "photo2",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "photo3",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "photo4",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "published_status",
                    models.BooleanField(
                        default=False,
                        help_text="Is property published?",
                        verbose_name="Published Status",
                    ),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Total Views")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="agent_buyer",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Agent, Seller or Buyer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="PropertyViews",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("ip", models.GenericIPAddressField(verbose_name="IP Address")),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_views",
                        to="properties.property",
                        verbose_name="Property",
                    ),
                ),
            ],
            options={
                "verbose_name": "Total Views on Property",
                "verbose_name_plural": "Total Property Views",
            },
        ),
    ]
