"""
Test search backend.
"""

from django.test import TestCase
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q

from .factories.summary import SummaryFactory
from ..serializers import SummariesDocument
from ..utils import rebuild_elasticsearch_index


class TestSummarySearch(TestCase):
    """Test search."""

    def setUp(self):
        self.es_client = Elasticsearch()
        self.search_instance = SummariesDocument.search()
        self.size = 2
        self.book_list = [SummaryFactory() for index in range(10)]

    def test_elastic_search_index_data(self):
        book = self.book_list[0]
        rebuild_elasticsearch_index()
        q = Q('bool', must=[Q('match', id=book.id), ])
        search_with_query = self.search_instance.query(q)
        response = search_with_query.execute()
        search_index_data = response.to_dict()['hits']['hits'][0]['_source']
        self.assertEqual(search_index_data['id'], book.id)

    def test_elastic_search_filter_summary_index(self):
        rebuild_elasticsearch_index()
        q = Q('bool', must=[Q('match', summary="what there"), ])
        search_with_query = self.search_instance.query(q).sort('_score')
        response = search_with_query.execute()
        list_doc = response.to_dict()['hits']['hits']

