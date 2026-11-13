from django.contrib.staticfiles.finders import find

import pytest


@pytest.mark.parametrize(
    "path",
    [
        pytest.param("venobox/css/venobox.min.css", id="css"),
        pytest.param("venobox/js/venobox.min.js", id="js"),
    ],
)
def test_static_assets_are_discoverable(path):
    assert find(path) is not None
