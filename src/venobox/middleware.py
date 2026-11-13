from functools import partial


def is_ajax(request):
    # VenoBox sends no X-Requested-With header,
    # so the browser-set Sec-Fetch-Dest is checked as well.
    headers = request.headers
    return (
        headers.get("X-Requested-With") == "XMLHttpRequest"
        or headers.get("Sec-Fetch-Dest") == "empty"
    )


class AjaxMiddleware:
    """Restore ``request.is_ajax()``, removed in Django 4.0."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.is_ajax = partial(is_ajax, request)
        return self.get_response(request)
