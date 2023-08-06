
Changelog
=========

1.0.0 (2023-01-10)
------------------

* Removed the ``runuwsgi`` management command as it was very broken.
  Yes, I've looked at `django-uwsgi-ng <https://pypi.org/project/django-uwsgi-ng/>`_
  (another fork, which has lots of changes for that command) and it's still pretty unusable in general (expects a certain project layout,
  and still generates weird if not broken configuration).

  Instead you should own your uWSGI configuration and not lets some tool generate it for you as some of the options have high impact on
  the behavior and performance of uWSGI.
* Fixed stats page title.
* Made clear cache and reload actions be performed safely over POST requests (previously they were GET requests).

0.3.0 (2023-01-09)
------------------

Forked from https://github.com/unbit/django-uwsgi this adds:

* Support for latest Django releases (3.2+).
* A basic integration test suite.
* Removed lots of old compat cruft.
* Integrated the uWSGI stats pane directly in the Django admin. Adding urls manually is no longer necessary.
* Removed the old wagtail-styled admin page (it was broken anyway).
