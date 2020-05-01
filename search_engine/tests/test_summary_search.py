"""
Test search backend.
"""

from django.core.management import call_command
from django.test import TestCase
from rest_framework import status
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q

from .factories.summary import SummaryFactory
from ..serializers import SummariesDocument


class TestSummarySearch(TestCase):
    """Test search."""

    def setUp(self):
        self.summary = SummaryFactory()
        self.es_client = Elasticsearch()
        self.search_instance = SummariesDocument.search()
        self.size = 2
        call_command('search_index', '--rebuild', '-f')

    def test_elastic_search_connection(self):
        q = Q('bool', must=[Q('match', summary="hello table"), ])
        search_with_query = self.search_instance.query(q).sort('_score')
        response = search_with_query.execute()
        list_doc = response.to_dict()['hits']['hits']

