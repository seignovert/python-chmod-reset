===============================
Reset Chmod
===============================
|Build| |Coverage| |PyPI| |Status| |Version| |Python| |License|

.. |Build| image:: https://travis-ci.org/seignovert/reset_chmod.svg?branch=master
        :target: https://travis-ci.org/seignovert/reset_chmod
.. |Coverage| image:: https://coveralls.io/repos/github/seignovert/reset_chmod/badge.svg?branch=master
        :target: https://coveralls.io/github/seignovert/reset_chmod?branch=master
.. |PyPI| image:: https://img.shields.io/badge/PyPI-reset_chmod-blue.svg
        :target: https://pypi.python.org/project/reset_chmod
.. |Status| image:: https://img.shields.io/pypi/status/reset_chmod.svg?label=Status
.. |Version| image:: https://img.shields.io/pypi/v/reset_chmod.svg?label=Version
.. |Python| image:: https://img.shields.io/pypi/pyversions/reset_chmod.svg?label=Python
.. |License| image:: https://img.shields.io/pypi/l/reset_chmod.svg?label=License

*Python package to reset chmod recursively*

Install
-------
With ``pip``:

.. code:: bash

    $ pip install reset_chmod

With the ``source files``:

.. code:: bash

    $ git clone https://github.com/seignovert/reset_chmod.git
    $ cd reset_chmod ; python setup.py install

Usage
------

.. code:: bash

    reset-chmod <FOLDER_NAME>

.. code:: python

    >>> import reset_chmod

    >>> reset_chmod.scan('.')
