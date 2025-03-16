import factory
from apps.profiles.models import Profile
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from real_estate.settings.base import AUTH_USER_MODEL

faker = FakerFactory.create()

@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('tests.factories.UserFactory')
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())