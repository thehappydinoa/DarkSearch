==========
DarkSearch
==========
.. image:: https://travis-ci.com/thehappydinoa/DarkSearch.svg?branch=master

Python API wrapper for `darksearch.io <https://darksearch.io/>`_

`API Documentation <https://darksearch.io/apidoc>`_

*******
Install
*******
.. code-block:: bash

  pip install darksearch

*****
Usage
*****
.. code-block:: python

  import darksearch

  results = darksearch.search("query")

  """
  `results` is a JSON dict object like this
  {
    "total": int,
    "per_page": int,
    "current_page": int,
    "last_page": int,
    "from": int,
    "to": int,
    "data": [
        {
            "title": string,
            "link": string,
            "description": string
        }
     ]
 }
  """

  results_page_2 = darksearch.search("query", page=2)

  """
  `results_page_2` is a JSON dict object like this
  {
    "total": int,
    "per_page": int,
    "current_page": 2,
    "last_page": int,
    "from": int,
    "to": int,
    "data": [
        {
            "title": string,
            "link": string,
            "description": string
        }
     ]
 }
  """

  results_pages = darksearch.search("query", pages=2)

  """
  `results_pages` is a list of JSON dict objects like this
  [
  {
    "total": int,
    "per_page": int,
    "current_page": 1,
    "last_page": int,
    "from": int,
    "to": int,
    "data": [
        {
            "title": string,
            "link": string,
            "description": string
        }
     ]
  },
  ...
  ]
  """

  results_pages = darksearch.search("query", pages=2, wait=2)

  """
  `wait` is the seconds between requests (DarkSearch's API is limited to 30 requests per minute.)
  `results_pages` is a list of JSON dict objects
  [
  {
    "total": int,
    "per_page": int,
    "current_page": 1,
    "last_page": int,
    "from": int,
    "to": int,
    "data": [
        {
            "title": string,
            "link": string,
            "description": string
        }
     ]
  },
  ...
  ]
  """
