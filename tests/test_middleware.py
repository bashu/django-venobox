from django.http import HttpResponse

import pytest

from venobox.middleware import AjaxMiddleware


@pytest.mark.parametrize(
    ("headers", "expected"),
    [
        pytest.param({"HTTP_SEC_FETCH_DEST": "empty"}, True, id="sec-fetch-xhr"),
        pytest.param({"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}, True, id="x-requested-with"),
        pytest.param({"HTTP_SEC_FETCH_DEST": "document"}, False, id="navigation"),
        pytest.param({}, False, id="no-headers"),
    ],
)
def test_is_ajax(rf, headers, expected):
    request = rf.get("/", **headers)
    response = HttpResponse()

    assert AjaxMiddleware(lambda _: response)(request) is response
    assert request.is_ajax() is expected
