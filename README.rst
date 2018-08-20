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

.. |docs| image:: https://readthedocs.org/projects/py-multihashing/badge/?version=latest
    :target: https://py-multihashing.readthedocs.io/en/latest/?badge=latest
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

Contributing
============

See our `contribution guidelines <CONTRIBUTING.rst>`_ for a development workflow and details on how to contribute.

Notes
=====

This module just makes working with multihashes a bit nicer. `py-multihash <//github.com/carsonfarmer/py-multihash>`_
is only for encoding/decoding multihashes, and does not depend on other libraries. This module will depend on various
implementations for each hash. It currently uses `pycryptodome` exclusively, but this will likely change as new hashing
functions are added (we're currently missing the MurmurHash3 functions, a double sha2-256 implementation, and all the
Skein functions).
