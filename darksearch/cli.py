import argparse
from pprint import pprint

from .api import Client


def encode(source):
    try:
        if isinstance(source, unicode):
            return source.encode('utf8')
    except NameError:
        return str(source)


def print_response(response):
    print("Current Page: {}".format(response.get("current_page")))
    print("")
    print("From: {}".format(response.get("from")))
    print("To: {}".format(response.get("to")))
    print("Per Page: {}".format(response.get("per_page")))
    print("Last Page: {}".format(response.get("last_page")))
    print("")
    print("Results: ")
    for result in response.get("data"):
        print("Title: {}".format(encode(result.get("title"))))
        print("Description: {}".format(encode(result.get("description"))))
        print("Link: {}".format(result.get("link")))
        print("")


def main():
    parser = argparse.ArgumentParser(description="DarkSearch API Client")
    parser.add_argument("-q", "--query", help="search query")
    parser.add_argument("-p", "--page", type=int, help="page number")
    parser.add_argument("-n", "--pages", type=int, help="number of pages")
    parser.add_argument("-w", "--wait", type=int, help="wait between requests")
    parser.add_argument("-j", "--json", action="store_true",
                        help="prints as json")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="prints verbose json")
    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        exit(1)

    client = Client(timeout=10)

    response = client.search(args.query, page=args.page,
                             pages=args.pages, wait=args.wait)

    if args.json:
        if args.verbose:
            print(response)
        else:
            pprint(response)
    else:
        if isinstance(response, list):
            for resp in response:
                print_response(resp)
        else:
            print_response(response)


if __name__ == "__main__":
    main()
