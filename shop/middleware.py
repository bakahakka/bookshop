from .models import WebRequest


class TrackWebRequestsMiddleware:
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
            uri=request.build_absolute_uri()
        ).save()

        return response
