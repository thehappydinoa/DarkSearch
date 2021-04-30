Usage
=====

.. code:: python

	from darksearch import Client

	c = Client()

	res = c.search("query")
	print(res)

	# Specify a optional page number
	res = c.search("query", page=3)
	print(res)

	# Specify several pages
	res = c.search("query", pages=2)
	print(res)

	# Return the number of indexed pages in DarkSearch.
	pages = c.crawling_status()
	print(pages)
