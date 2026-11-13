Changes
-------

0.2.0 (2026-11-13)
~~~~~~~~~~~~~~~~~~

* Add ``venobox.middleware.AjaxMiddleware``, which restores ``request.is_ajax()`` removed in Django 4.0.
  It also detects VenoBox requests, which carry ``Sec-Fetch-Dest: empty`` instead of ``X-Requested-With``.
* Switch packaging to ``hatchling`` and the ``src`` layout.

0.1.2 (2026-10-10)
~~~~~~~~~~~~~~~~~~

* Drop support for Python 3.10; Python 3.11 is now the minimum required version.
* Add support for Python 3.15.

0.1.0 (2026-09-08)
~~~~~~~~~~~~~~~~~~

* Initial release.
