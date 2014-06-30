

import logging

from django.conf import settings


def get_logger(name):
    prefix = getattr(settings, 'LOGGER_PREFIX', 'apps')
    return logging.getLogger('{}.{}'.format(prefix, name))
