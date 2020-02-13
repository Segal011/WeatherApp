import logging

logging.basicConfig(level=logging.DEBUG)


class SimpleMiddleware:
    def __init__(self, get_response): # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        logging.info(response)

        # Code to be executed for each request/response after
        # the view is called.

        return response
