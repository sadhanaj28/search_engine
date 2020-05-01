from django.test import TestCase
from faker import Factory
from search_engine.tests.factories.summary import SummaryFactory

# faker = Factory.create()


class SummaryTests(TestCase):

    def setUp(self):
        self.summary = SummaryFactory()

    def test_curd_summary(self):
        summary_f = self.summary
        self.assertEqual(summary_f.pk, summary_f.id)

