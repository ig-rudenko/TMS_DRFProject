from django.core.handlers.wsgi import WSGIRequest
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request: WSGIRequest):
        print("process_request", request.path, request.META)
