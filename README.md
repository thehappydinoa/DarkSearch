# DarkSearch

[![PyPI](https://img.shields.io/pypi/v/darksearch?color=orange&logo=pypi&logoColor=orange)](https://pypi.org/project/darksearch/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?logo=python)](https://www.python.org/downloads/)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/thehappydinoa/DarkSearch/test?label=tests)](https://github.com/thehappydinoa/DarkSearch/actions)
[![License](https://img.shields.io/github/license/thehappydinoa/DarkSearch)](LICENSE)

Python API wrapper for DarkSearch ([darksearch.io](https://darksearch.io/)).

## Install

```bash
pip install darksearch
```

## Cli

```bash
darksearch --query "query" --page 1

darksearch --query "query" --pages 2

darksearch --query "query" --pages 2 --wait 2

darksearch --query "query" --json
```

## Usage

```python
import darksearch

 """
 `timeout`, `headers`, and `proxies`  are optional
 timeout = 10
 proxies = {
     "http": "http://127.0.0.1:8080"
 }
 headers = {
     "User-Agent": "Chrome/57.0.2987.133"
 }
 """

client = darksearch.Client(timeout=30, headers=None, proxies=None)

results = client.search("query")

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

results = client.search("query", page=2)

 """
 `results` is a JSON dict object like this
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

results = client.search("query", pages=2)

 """
 `results` is a list of JSON dict objects like this
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

results = client.search("query", pages=2, wait=2)

 """
 `wait` is the seconds between requests (DarkSearch's API is limited to 30 requests per minute.)
 `results` is a list of JSON dict objects
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

crawling_status = darksearch.crawling_status()

 """
 `crawling_status` is a integer of pages that have been indexed
 """
```

[Proxies Documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies)

## Testing

```bash
pytest
```
