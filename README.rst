===========================
Emencia Django French Zones
===========================

French regions and departments utilities for your Django projects.

.. contents::

Installation
============

You could retrieve the last sources from http://github.com/Fantomas42/emencia-django-french_zones and running the installation script ::
    
  $> python setup.py install

or use pip ::

  $> pip install -e git://github.com/Fantomas42/emencia-django-french_zones.git#egg=emencia.django.french_zones


In your projects
================

Register **emencia.django.french_zones** in your INSTALLED_APPS section your project settings. ::

  >>> INSTALLED_APPS = (
  ...   # Your favorites apps
  ...   'emencia.django.french_zones',
  ... )

Now you can run a *syncdb* for installing the models into your database and all the french regions with her departments associated contained in a fixture.


Usage
=====

With the fixture loaded on the database you can easily retrieve the **Department** and the **Region** associated with a french postal code. ::

  >>> from emencia.django.french_zones.utils import get_region_from_postal_code
  >>> from emencia.django.french_zones.utils import get_department_from_postal_code

  >>> get_department_from_postal_code('62138')
  ... <Department: Pas-de-Calais>

  >>> get_region_from_postal_code('62138')
  ... <Region: Nord Pas-de-Calais>

