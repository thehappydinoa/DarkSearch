==========
DarkSearch
==========

Python API wrapper for `darksearch.io <https://darksearch.io/>`_

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

  response = darksearch.search("query")

  """
  Returns JSON object formatted like this:
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
