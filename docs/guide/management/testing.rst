Testing
=======

Overview
--------

Open Budget has a suite of tests, with the goal of moving to 100% coverage of project code.

We view tests as an integral part of contributing code to the project: any code contributions must be accompanied by tests.

A great way to get into the codebase is to run the tests, read the tests, and extend them, refactor them, or raise issues on the issue tracker for potential problems.

Configuration
-------------

There are no specific configurations for testing. Please see Depenedncies below for more information.

Running Tests
-------------

To run all the tests of the project::

    python manage.py selftest

Also, when you use devstrap to bootstrap a local environment, you can use the -t flag to run tests::

    python manage.py devstrap -m -t

Dependencies
------------

Open Budget tests depend on the following 3rd party packages:

* django
* factory boy

Django
~~~~~~

https://github.com/django/django

Django comes with its own test framework. There is extensive documentation for this on the Django site. Please get very familiar with the docs if you will be contributing code to Open Budget:

https://docs.djangoproject.com/en/1.5/topics/testing/

How to import::

    from django.test import TestCase

Example implementation:

https://github.com/hasadna/omuni-budget/blob/develop/openbudget/apps/international/tests.py

Factory Boy
~~~~~~~~~~~

https://github.com/dnerdy/factory_boy

Factory Boy is a Python package for creating test objects. It has great support for Django, but can be used in any Python codebase.

We use Factory Boy to create mock objects for models. Our tests use these mock objects, and not fixtures.

All definitions for mock objects are found in "factories.py" modules, per app.

Please refer to the Factory Boy documentation if you will be contrinuting code to Open Budget:

http://factoryboy.readthedocs.org/en/latest/

How to import::

    import factory

Example implementation:

https://github.com/hasadna/omuni-budget/blob/develop/openbudget/apps/budgets/factories.py

Project Code
------------

Following Django and Factory Boy conventions, tests are in 'tests.py' modules in each app that has tests, and factories are in 'factories.py' modules for the same.





