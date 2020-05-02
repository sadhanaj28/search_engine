"""
documents.py, specifing elastic_search Document for model
It is used for
1) specify elastic_search index for specific model
2) specify the field type and feature for index
3) set number_of_shards and number_of_replicas for elastic_search index

"""

from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections

from .models import Summaries

# create the connection with ELASTICSEARCH server
connections.create_connection(hosts=['localhost'])

# elastic_search analyzer setup
html_strip = analyzer('html_strip',
                      tokenizer="standard",
                      filter=["lowercase", "stop", "snowball"],
                      char_filter=["html_strip"]
                      )


@registry.register_document
class SummariesDocument(Document):

    # The fields of the model you want to be indexed in Elastic_search
    id = fields.IntegerField(attr='id')
    summary = fields.TextField(
        analyzer=html_strip,
        fields={'raw': fields.TextField(), }
    )

    class Index:

        # Name of elastic_search index for Summaries model
        name = 'summary_data'

        # basic setup for elasticsearch
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:

        # the model name
        model = Summaries
