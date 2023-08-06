Bankline Direct Parser
======================

Python module for parsing Natwest/RBS Bankline Direct Data Services files.


Requirements
------------

Only Python 3.7+ is supported.


Installation
------------

.. code-block:: shell

    pip install bankline-direct-parser


Usage
-----

.. code-block:: python

    from bankline_parser.data_services import parse

    # from file
    with open(filename) as f:
        parsed = parse(f)
        if parsed.is_valid():
            print(parsed.accounts[0].records[0].transaction_code)
        else:
            print(parsed.errors)

    # from list of rows
    parsed = parse(lines)


Model Layout
------------

.. code-block::

    DataServicesFile
        VolumeHeaderLabel
        [Account]
            FileHeaderLabel
            UserHeaderLabel
            [DataRecord|BalanceRecord]
            UserTrailerLabel


Development
-----------

.. image:: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/test.yml

.. image:: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/lint.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/lint.yml

Please report bugs and open pull requests on `GitHub`_.

Use ``python setup.py test`` or ``tox`` to run all tests.

Distribute a new version by updating the ``VERSION`` tuple in ``bankline_parser/__init__.py`` and
publishing a release in GitHub (this triggers a GitHub Actions workflow to automatically upload it).
Alternatively, run ``python setup.py sdist bdist_wheel upload`` locally.
Remember to update `History`_.


History
-------

0.7
    Maintenance release, no library changes.

0.2 - 0.6
    No significant library changes, other than support for newer versions of python.

0.1
    Original release.


Copyright
---------

Copyright (C) 2023 HM Government (Ministry of Justice Digital & Technology).
See LICENSE.txt for further details.

.. _GitHub: https://github.com/ministryofjustice/bankline-direct-parser
