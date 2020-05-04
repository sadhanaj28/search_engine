"""unit test for models"""
from django.test import TestCase
from .factories.summary import SummaryFactory


class SummaryTests(TestCase):

    def setUp(self):
        self.summary = SummaryFactory()

    def test_get_summary(self):

        summary_f = self.summary
        self.assertEqual(summary_f.pk, summary_f.id)

