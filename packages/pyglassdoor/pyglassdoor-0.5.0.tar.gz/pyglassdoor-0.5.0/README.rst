===========
PyGlassdoor
===========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel|
        | |supported-versions| |supported-implementations|
        | |commits-since| |downloads|
.. |docs| image:: https://readthedocs.org/projects/pyglassdoor/badge/?style=flat
    :target: https://pyglassdoor.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/hamid-vakilzadeh/pyglassdoor/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/hamid-vakilzadeh/pyglassdoor/actions

.. |codecov| image:: https://codecov.io/gh/hamid-vakilzadeh/pyglassdoor/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/hamid-vakilzadeh/pyglassdoor

.. |version| image:: https://img.shields.io/pypi/v/pyglassdoor.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pyglassdoor

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyglassdoor.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pyglassdoor

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyglassdoor.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pyglassdoor

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyglassdoor.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pyglassdoor

.. |commits-since| image:: https://img.shields.io/github/commits-since/hamid-vakilzadeh/pyglassdoor/v0.5.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hamid-vakilzadeh/pyglassdoor/compare/v0.5.0...master

.. |downloads| image:: https://static.pepy.tech/personalized-badge/pyglassdoor?period=total&units=abbreviation&left_color=yellowgreen&right_color=grey&left_text=Downloads
    :target: https://pepy.tech/project/pyglassdoor

.. end-badges

Overview
============

Python API for glassdoor.com.


Installation
~~~~~~~~~~~~

.. code:: bash

    pip install pyglassdoor


Example
~~~~~~~

The example below shows the code for downloading 20 reviews of Apple company.

First, we need the ``company_id`` of Apple. We can find this number in the URL link of
Apple's ``overview`` page on glassdoor.

https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm

``company_id`` for Apple is ``1138`` which is the number right after ``IE``.

.. code:: python

    import pyglassdoor as gd

    # download 20 reviews of APPLE Inc.
    query = gd.get_reviews(company_id=1138, records_to_collect=20)

    # query is in json format and contains all the information about reviews.
    # We can access the reviews as follows
    apple_reviews = query['employerReviews']['reviews']

    # and for example convert to dataframe
    df = pd.DataFrame(apple_reviews)

Documentation
=============


https://pyglassdoor.readthedocs.io/


Development
===========

To run all the tests run::

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

