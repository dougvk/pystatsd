try:
    from django.conf import settings
except ImportError:
    settings = None

from client import StatsClient


__all__ = ['StatsClient', 'statsd', 'VERSION']

VERSION = (0, 1)


if settings:
    host = getattr(settings, 'STATSD_HOST', 'localhost')
    port = getattr(settings, 'STATSD_PORT', 8125)
    statsd = StatsClient(host, port)