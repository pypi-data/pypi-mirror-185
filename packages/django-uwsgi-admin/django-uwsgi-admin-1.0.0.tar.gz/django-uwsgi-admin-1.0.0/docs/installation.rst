============
Installation
============


At the command line::

    pip install django-uwsgi-admin


By default ``django-uwsgi`` doesn't require uWSGI as requirement. And here are a few known reasons why:

* Django project is installed into virtualenv and ran in `Emperor <http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html>`_ mode.
  In this case uWSGI is installed system-wide or into some other virtualenv.
* Some devs love to use system package managers like apt and prefer to install uwsgi other way.
* You need to build uWSGI with custom profile ex: ``UWSGI_PROFILE=gevent pip install uwsgi``

You can install django-uwsgi with uWSGI by appending ``[uwsgi]`` to the install command:

.. code:: bash

    pip install 'django-uwsgi-admin[uwsgi]'
