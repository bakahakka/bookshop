from django.utils import timezone
from .models import WebRequest


class TrackWebRequestsMiddleware:
    """
    Tracking each HTTP request excluding admin or favicon requests
    Saving the request data to database
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/admin') or request.path.endswith('/favicon.ico'):
            return response

        WebRequest(
            path=request.path,
            method=request.method,
            status_code=response.status_code,
            uri=request.build_absolute_uri(),
            time=timezone.now()
        ).save()

        return response
