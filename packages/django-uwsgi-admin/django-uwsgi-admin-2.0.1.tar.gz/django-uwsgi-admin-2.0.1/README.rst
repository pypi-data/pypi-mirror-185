========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/django-uwsgi-admin/badge/?style=flat
    :target: https://django-uwsgi-admin.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/ionelmc/django-uwsgi-admin/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/django-uwsgi-admin/actions

.. |requires| image:: https://requires.io/github/ionelmc/django-uwsgi-admin/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/django-uwsgi-admin/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/ionelmc/django-uwsgi-admin/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/django-uwsgi-admin

.. |version| image:: https://img.shields.io/pypi/v/django-uwsgi-admin.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/django-uwsgi-admin

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-uwsgi-admin.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/django-uwsgi-admin

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-uwsgi-admin.svg
    :alt: Supported versions
    :target: https://pypi.org/project/django-uwsgi-admin

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-uwsgi-admin.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/django-uwsgi-admin

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/django-uwsgi-admin/v2.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/django-uwsgi-admin/compare/v2.0.1...master



.. end-badges

Django related examples/tricks/modules for uWSGI.

* Free software: MIT license

Installation
============

::

    pip install django-uwsgi-admin

You can also install the in-development version with::

    pip install https://github.com/ionelmc/django-uwsgi-admin/archive/master.zip


Documentation
=============

https://django-uwsgi-admin.readthedocs.io/

Screenshots
===========

`django-debug-toolbar <http://django-debug-toolbar.readthedocs.org/en/latest/>`_ panel

.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot1.png

`Wagtail <https://github.com/torchbox/wagtail>`_ admin interface:

.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot2.png

`django.contrib.admin <https://docs.djangoproject.com/en/1.10/ref/contrib/admin/>`_ interface

.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot3.png
.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot4.png
.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot5.png
.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot6.png
.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot7.png
.. image:: https://github.com/ionelmc/django-uwsgi-admin/raw/master/docs/screenshots/screenshot8.png

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
