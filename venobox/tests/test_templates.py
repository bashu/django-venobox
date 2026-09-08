from django.contrib.staticfiles.finders import find
from django.test import TestCase


class VenoboxTemplateTest(TestCase):
    def test_static_assets_are_discoverable(self):
        assert find("venobox/css/venobox.min.css") is not None
        assert find("venobox/js/venobox.min.js") is not None
