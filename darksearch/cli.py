from argparse import ArgumentParser
from pprint import pprint

from .api import Client


def print_response(response: dict):
    """Print the response from the API.

    :param response: the API response
    :type response: dict
    """
    print("Current Page: {}\n".format(response.get("current_page")))
    print("From: {}".format(response.get("from")))
    print("To: {}".format(response.get("to")))
    print("Per Page: {}".format(response.get("per_page")))
    print("Last Page: {}\n".format(response.get("last_page")))
    print("Results: ")
    data = response.get("data", [])
    for result in data:
        print("Title: {}".format(result.get("title")))
        print("Description: {}".format(result.get("description")))
        print("Link: {}\n".format(result.get("link")))


def main():
    """Execute this command line."""
    parser = ArgumentParser(description="DarkSearch API Client")
    parser.add_argument("-q", "--query", help="search query")
    parser.add_argument("-p", "--page", type=int, help="page number")
    parser.add_argument("-n", "--pages", type=int, help="number of pages")
    parser.add_argument("-w", "--wait", type=int, help="wait between requests")
    parser.add_argument("-j", "--json", action="store_true", help="prints as json")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="prints verbose json"
    )
    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        exit(1)

    client = Client(timeout=10)

    response = client.search(
        args.query, page=args.page, pages=args.pages, wait=args.wait
    )

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
