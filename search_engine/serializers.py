from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import SummariesDocument


# firsst priority
class SummariesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = SummariesDocument
        fields = (
            'id',
            'summary',
        )
