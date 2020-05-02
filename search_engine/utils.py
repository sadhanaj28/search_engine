"""
utils file, contains code which are generic
"""
from django.core.management import call_command


def is_empty_or_null(value):
    if (not value) or (value == '') or (value is None) or (value == 'null'):
        return True
    return False


# run elastic search command to rebuild index
def rebuild_elasticsearch_index():
    call_command('search_index', '--rebuild', '-f')


# run elastic search command to delete index
def delete_elasticsearch_index():
    call_command('search_index', '--delete', '-f')
