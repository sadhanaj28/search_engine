import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import elasticsearch
from .documents import SummariesDocument

from .helps import ElasticSearchBookService
from .utils import is_empty_or_null

import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


class SearchEXP(APIView):

    def post(self, request):
        query_list = request.data.get('queries', None)
        k = request.data.get('k', None)
        response = None

        if is_empty_or_null(query_list):
            error_message = "queries should be string/list of string and not empty"
            return Response({"error_message": error_message})

        if is_empty_or_null(k):
            error_message = "k should be integer and not empty"
            return Response({"error_message": error_message})

        try:
            search_doc = ElasticSearchBookService(SummariesDocument, query_list, k)
            result = search_doc.run_query_list()
            response = {'books': result}
        except elasticsearch.ConnectionError as ce:
            logger.debug('ConnectionError: ' + str(ce))
            error_message = "Elasticsearch Connection refused"
            return Response({"error_message": error_message})
        except elasticsearch.ElasticsearchException as ee:
            logger.debug('ElasticsearchException: ' + str(ee))
            error_message = "Elasticsearch Connection refused"
            return Response({"error_message": error_message})
        except Exception as e:
            logger.debug('Exception: ' + str(e))
            error_message = str(e)
            return Response({"error_message": error_message})

        return Response(response)

