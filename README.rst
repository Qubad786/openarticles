Developing & Testing
--------------------

Major Requirements:
 - Python3.6
 - Django2.0

First, create a virtual environment and install requirements:

.. code-block:: bash

    virtualenv ~/.virtualenvs/openarticles
    source ~/.virtualenvs/openarticles/bin/activate
    pip install -r requirements.txt

Run migrations and collect static assets:

.. code-block:: bash

    python manage.py migrate
    python manage.py collectstatic

Create a superuser to access Django Administration Console (i.e. /admin):

.. code-block:: bash

    python manage.py create_admin # This will also print superuser credentials.


Finally, run development server as follow:

.. code-block:: bash

    python manage.py runserver 0.0.0.0:8080


Now, you will be able to visit Open Articles @ http://localhost:8080 and Django Admin @ http://localhost:8080/admin
