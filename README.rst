lib_parameter
=============


Version v1.1.15 as of 2023-07-14 see `Changelog`_

|build_badge| |codeql| |license| |jupyter| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_parameter/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_parameter/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/lib_parameter/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/lib_parameter/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_parameter/master?filepath=lib_parameter.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-parameter?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_parameter

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_parameter
   :target: https://codecov.io/gh/bitranox/lib_parameter

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_parameter?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_parameter/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_parameter?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_parameter/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_parameter?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_parameter/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/lib_parameter/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_parameter

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-parameter
   :target: https://pypi.org/project/lib-parameter/
   :alt: PyPI - Downloads

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

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, 3.12-dev, pypy-3.9, pypy-3.10 - architectures: amd64

`100% code coverage <https://codeclimate.com/github/bitranox/lib_parameter/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_parameter/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_parameter/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_parameter/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_parameter/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_parameter.ipynb>`_

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time

Usage from Commandline
------------------------

.. code-block::

   Usage: lib_parameter [OPTIONS] COMMAND [ARGS]...

     small gist,to return a default value if the parameter is None

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_parameter


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade lib_parameter[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_parameter.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_parameter

    # for the latest development version :
    lib_parameter @ git+https://github.com/bitranox/lib_parameter.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_parameter.git
    $ cd lib_parameter
    python -m pip install -e .[test]

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

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools
    lib_detect_testenv

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

v1.1.15
---------
2023-07-14:
    - add codeql badge
    - move 3rd_party_stubs outside the src directory to ``./.3rd_party_stubs``
    - add pypy 3.10 tests
    - add python 3.12-dev tests

v1.1.14
---------
2023-07-13:
    - require minimum python 3.8
    - remove python 3.7 tests

v1.1.13
---------
2023-07-13:
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config
    - clean ./tests/test_cli.py

v1.1.12.2
---------
2022-06-01: update to github actions checkout@v3 and setup-python@v3

v1.1.12.1
---------
2022-06-01: update github actions test matrix

v1.1.12
--------
2022-03-29: remedy mypy Untyped decorator makes function "cli_info" untyped

v1.1.11
--------
2022-03-25: fix github actions windows test

v1.1.10
-------
2021-11-22
    - fix "setup.py test"

v1.1.9
------
2021-11-21: service release
    - implement github actions
    - implement check for test environment on __init__

v1.1.8
--------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.1.7
---------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.1.6
---------
2020-08-07: fix wheels

v1.1.5
---------
2020-08-01: fix pypi deploy

v1.1.4
-------
2020-07-31: initial PyPi release

