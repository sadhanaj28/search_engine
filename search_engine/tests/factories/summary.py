import factory
from faker import Factory

from ...models import Summaries

faker = Factory.create()


class SummaryFactory(factory.DjangoModelFactory):

    class Meta:
        model = Summaries

    summary = faker.text()
