========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|

.. |docs| image:: https://readthedocs.org/projects/py-multihashing/badge/?style=flat
    :target: https://readthedocs.org/projects/py-multihashing
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/carsonfarmer/py-multihashing.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/carsonfarmer/py-multihashing

.. |requires| image:: https://requires.io/github/carsonfarmer/py-multihashing/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/carsonfarmer/py-multihashing/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/carsonfarmer/py-multihashing/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/carsonfarmer/py-multihashing

.. |codecov| image:: https://codecov.io/github/carsonfarmer/py-multihashing/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/carsonfarmer/py-multihashing


.. end-badges

Use all the functions in multihash

This module just makes working with multihashes a bit nicer.
`py-multihash <//github.com/carsonfarmer/py-multihash>`_ is only for
encoding/decoding multihashes, and does not depend on other libraries.
This module will depend on various implementations for each hash.
It currently uses `hashlib` exclusively, but this will likely change
as new hashing functions are added (we're currently missing the
MurmurHash3 functions, a double sha2-256 implementation, and all the
Keccak and Skein functions).

License
=======

`MIT Licensed <LICENSE>`_ © 2018 Carson Farmer, 2016 Protocol Labs Inc.

Installation
============

::

    pip install git+https://github.com/carsonfarmer/py-multihashing

Documentation
=============

https://py-multihashing.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox