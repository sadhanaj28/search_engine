from django.core.management import call_command


def is_empty_or_null(value):
    if (not value) or (value == '') or (value is None) or (value == 'null'):
        return True
    return False


def rebuild_elasticsearch_index():
    call_command('search_index', '--rebuild', '-f')


def delete_elasticsearch_index():
    call_command('search_index', '--delete', '-f')
