from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Text, fields, Keyword
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
# from django_elasticsearch_dsl_drf import fields

from .models import Summaries


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

html_strip = analyzer('html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class SummariesDocument(Document):
    id = fields.IntegerField(attr='id')
    summary = fields.TextField(
        analyzer=html_strip,
        fields={'raw': fields.TextField(), }
    )
    # summary = Text(
    #     analyzer=html_strip,
    #     fields={'raw': Keyword()}
    # )


    class Index:
        # Name of elasticsearch index
        name = 'summary_data'

        # see the Elasticssearch indices API reference for available settings.
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:

        # this model associated with this doc
        model = Summaries
