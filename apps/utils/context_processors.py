
from django.conf import settings

def google_analytics(request):
    """
    Provides Google Analytics Template Context
    """
    return {
        'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY,
        'GOOGLE_ANALYTICS_DOMAIN': settings.GOOGLE_ANALYTICS_DOMAIN,
    }


def bugherd(request):
    """
    Provides Bugherd Template Context
    """
    return {
        'BUGHERD_KEY': settings.BUGHERD_KEY,
    }
