======================
Installing valorant.py
======================

The following guide will walk you through the steps need to install ``valorant.py`` in your enviornment.


Standard Installation
~~~~~~~~~~~~~~~~~~~~~

``valorant.py`` can be obtained normally from `PyPI <https://pypi.org/>`_ using PIP: ::

    pip install valorant

The package is also available from the GitHub repository: ::

    pip install git+https://github.com/frissyn/valorant.py

Of course, you can specify version tags as well: ::

    pip install git+https://github.com/frissyn/valorant.py@v0.5.1


Bleeding Edge
~~~~~~~~~~~~~

If you'd like the bleeding edge version of ``valorant.py``, it's available from the ``dev`` branch of the GitHub repository. This version isn't guaranteed to be stable or documented very well, as this is the branch I work on in real time when adding features, bug fixing, etc. ::

    pip install git+https://github.com/frissyn/valorant.py@dev

Virtual Enviornments
~~~~~~~~~~~~~~~~~~~~

Sometimes you need to prevent a package from polluting other enviornments on the system, or install multiple versions of the same package. Whatever the use case, Python 3 provides a standard utility for creating virtual enviornments for just that purpose. See the official `Virtual Enviornments and Packages <https://docs.python.org/3/tutorial/venv.html>`_ page for more in-depth documentation.

1. Enter your project's working (top-level) directory:

    .. code-block:: shell

        $ cd my-project
        $ python -m venv project-env

2. Activate the virtual enviornment:

    .. code-block:: shell

        $ source project-env/bin/activate

    On a non-Unix system (*cough*, Windows):

    .. code-block:: shell

        $ project-env\Scripts\active.bat

3. Then use ``pip`` as you normally would!

    .. code-block:: shell

        $ pip install valorant
