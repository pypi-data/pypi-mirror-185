
Changelog
=========


2.0.1 (2023-01-13)
------------------

* UwsgiWorkersPanel no longer tries to generate stats if there's no uwsgi.

2.0.0 (2023-01-12)
------------------

* Removed the decorators module, something that only existed to avoid installing a separate package. Instead you should install the updated
  `uwsgidecorators <https://pypi.org/project/uwsgidecorators/>`_ package.
* Removed ``django_uwsgi.template.Loader`` (and the whole module) as it was broken and pretty hard to test without a custom build of uWSGI.
* Split all sections in the Status page into seperate admin pages: Actions, Applications, Jobs, Magic Table, Options, Status and Workers.
* Removed the old django debug toolbar and replaced with 2 new panes:

  * ``django_uwsgi.panels.UwsgiWorkersPanel``
  * ``django_uwsgi.panels.UwsgiActionsPanel``

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
