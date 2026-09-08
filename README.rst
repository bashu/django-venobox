django-venobox
===============


.. image:: https://badge.fury.io/py/django-venobox.svg
    :target: https://badge.fury.io/py/django-venobox

.. image:: https://img.shields.io/pypi/pyversions/django-venobox.svg
    :target: https://pypi.python.org/pypi/django-venobox/

.. image:: https://img.shields.io/pypi/djversions/django-venobox.svg
    :target: https://pypi.python.org/pypi/django-venobox/

.. image:: https://github.com/bashu/django-venobox/actions/workflows/test.yml/badge.svg
    :target: https://github.com/bashu/django-venobox/actions/workflows/test.yml

This is a Django_ integration of VenoBox_.

Installation
------------

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install django-venobox

Setup
-----

Add ``venobox`` to  ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'venobox',
    )

Be sure you have the ``django.template.context_processors.request`` processor

.. code-block:: python

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

and just include ``venobox`` templates

.. code-block:: html+django

    {% include "venobox/venobox_css.html" %} {# Before the closing head tag #}
    {% include "venobox/venobox_js.html" %} {# Before the closing body tag #}

When deploying on production server, don't forget to run :

.. code-block:: shell

    python manage.py collectstatic

Usage
-----

Extend base template for ajax requests

.. code-block:: html+django

    {% extends request.is_ajax|yesno:"venobox/base.html,base.html" %}

Add ``class="venobox"`` to a link, and set the href to a page you want to display

.. code-block:: html+django

    <a data-vbtype="ajax" href="{% url 'remote.html' %}" class="venobox">Click here</a>

Please see ``example`` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

License
-------

``django-venobox`` is released under the BSD license.

.. _django: https://www.djangoproject.com/
.. _venobox: https://veno.es/venobox/
