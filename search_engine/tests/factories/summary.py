import factory
from faker import Factory

from ...models import Summaries

faker = Factory.create()

# But not default locales
# factory.Faker.override_default_locale('es_ES')
# if locale is None:
# locale = factory.Faker._DEFAULT_LOCALE
# factory.Faker.add_provider(locale)
class SummaryFactory(factory.DjangoModelFactory):

    class Meta:
        model = Summaries

    summary = faker.text()
