"""
View file
"""
import logging
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import elasticsearch

from .documents import SummariesDocument
from .helps import ElasticSearchBookService
from .utils import is_empty_or_null, rebuild_elasticsearch_index, delete_elasticsearch_index

# Get an instance of a logger
logger = logging.getLogger(__name__)


class SummarySearchView(APIView):

    """
    format the response with message, status, data
    and send as api response
    """
    def __send_response(self, message, status_code, data=None):
        content = {
            "message": message,
            "result": data if data is not None else []
            }
        return Response(content, status=status_code)

    """
    handle post request
    filter the sammmaries data based on given query list with k number 
    """
    def post(self, request):
        query_list = request.data.get('queries', None)
        k = request.data.get('k', None)
        # response = None

        if is_empty_or_null(query_list):
            error_message = "queries should not be empty"
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)
        if type(query_list) != list:
            error_message = "queries should be list of query/keywords"
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        if is_empty_or_null(k):
            error_message = "k should be integer and not empty"
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        try:
            # build elastic search index
            rebuild_elasticsearch_index()

            # build search instance using SummariesDocument and save query_list and k as instance value
            search_doc = ElasticSearchBookService(SummariesDocument, query_list, k)

            # run each query using search instance
            result = search_doc.run_query_list()
            response = {'books': result}

            # delete elastic search index
            delete_elasticsearch_index()

        except elasticsearch.ConnectionError as connection_error:
            # ConnectionError if elasticsearch server is down
            logger.debug('ConnectionError: ' + str(connection_error))
            error_message = "Elastic search Connection refused"
            return self.__send_response(error_message, status.HTTP_503_SERVICE_UNAVAILABLE)

        except Exception as exception_msg:
            # handle all type of error
            logger.debug('Exception: ' + str(exception_msg))
            error_message = str(exception_msg)
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        return self.__send_response('success', status.HTTP_200_OK, response)

