=====
First Atlantic Commerce Payment Integration
=====

django-fac is a Django app to conduct that is used to integrate with First Atlantic Commerce payment gateway

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_fac" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_fac',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('payment/', include('django_fac.urls')),

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/payment/health/ to test the integration.