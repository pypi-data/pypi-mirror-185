========================
Django Crud Library
========================

my-django-crud is a python library built using django rest framework that enables you perform CRUD functionalities on
your Django models without writing serializer classes and view functions.

Quick Start
===========

1. Add "DjangoCrud" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'DjangoCrud',
    ]

2. Import view functions from DjangoCrud in your urls.py like this:
    from DjangoCrud import views

3. Specify the url paths like below::

    urlpatterns = [
        path('create/', views.create(my_model), name='create'),
        path('list/', views.list(my_model), name='list'),
        path('update/<str:pk>', views.update(my_model), name='update'),
        path('detail/<str:pk>', views.detail(my_model), name='detail'),
        path('delete/<str:pk>', views.delete(my_model), name='delete')

    ]

NOTE
=====
Replace "my_model" with your own model 