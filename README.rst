lib_parameter
=============

|travis_build| |license| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/lib_parameter/master.svg
   :target: https://travis-ci.org/bitranox/lib_parameter

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_parameter/master?filepath=jupyter_test_lib_parameter.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-parameter?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_parameter


.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_parameter
   :target: https://codecov.io/gh/bitranox/lib_parameter

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_parameter?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_parameter

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_parameter?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_parameter/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_parameter?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_parameter/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_parameter?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_parameter/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/lib_parameter
   :target: https://snyk.io/test/github/bitranox/lib_parameter

small gist, to return a default value if the parameter is None

for mypy type annotation, the parameter usually has the type **Optional[T]**, the returned type will have the type **T**

really not worth a package, just dont know where else to put it.


.. code-block:: python

    # definition
    from typing import TypeVar, Optional

    T = TypeVar('T')

    def get_default_if_none(parameter: Optional[T], default: T) -> T:
        if parameter is None:
            return default
        else:
            return parameter


.. code-block:: python

    # usage
    from typing import Optional
    import lib_parameter

    x: Optional[int] = None

    x = lib_parameter.get_default_if_none(x, default=1)
    # now x is from type int, not Optional[int]

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`100% code coverage <https://codecov.io/gh/bitranox/lib_parameter>`_, codestyle checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/lib_parameter>`_, automatic daily builds and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_parameter/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_parameter/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_parameter/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----



Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    # install latest release from PyPi
    python -m pip install --upgrade lib_parameter

    # test latest release from PyPi without installing (can be skipped)
    python -m pip install lib_parameter --install-option test

- to install the latest development version from github via pip:


.. code-block:: bash

    # normal install
    python -m pip install --upgrade git+https://github.com/bitranox/lib_parameter.git

    # to test without installing (can be skipped)
    python -m pip install git+https://github.com/bitranox/lib_parameter.git --install-option test

    # to install and upgrade all dependencies regardless of version number
    python -m pip install --upgrade git+https://github.com/bitranox/lib_parameter.git --upgrade-strategy eager


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_parameter

    # for the latest development version :
    lib_parameter @ git+https://github.com/bitranox/lib_parameter.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt



- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_parameter.git
    $ cd lib_parameter

    # to test without installing (can be skipped)
    python setup.py test

    # normal install
    python setup.py install

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_parameter.git
    $ cd lib_parameter

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time

Usage from Commandline
------------------------

.. code-block:: bash

   Usage: lib_parameter [OPTIONS] COMMAND [ARGS]...

     small gist,to return a default value if the parameter is None

   Options:
     --version   Show the version and exit.
     -h, --help  Show this message and exit.

   Commands:
     info  get program informations

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_parameter/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes


0.0.3
-----
2020-07-06 : patch release
    - new click cli
    - use PizzaCutter Template

0.0.2
-----
2019-09-02: refractor

0.0.1
-----
2019-09-02: Initial public release

