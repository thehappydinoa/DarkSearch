from argparse import ArgumentParser
from pprint import pprint
from typing import List

from rich import print
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree

from .api import Client


def print_response(responses: List[dict]):
    """Print the response from the API.

    :param response: the API response
    :type response: dict
    """
    for response in responses:
        page_tree = Tree("Page {}\n".format(response.get("current_page")))
        page_tree.add("From: {}".format(response.get("from")))
        page_tree.add("To: {}".format(response.get("to")))
        page_tree.add("Per Page: {}".format(response.get("per_page")))
        page_tree.add("Last Page: {}\n".format(response.get("last_page")))
        results_tree = page_tree.add("Results")
        for result in response.get("data", []):
            result_branch = results_tree.add(Text(result.get("title"), "purple"))
            description_branch = result_branch.add("📜 Description")
            description_branch.add(Panel(Markdown(result.get("description"))))
            link_branch = result_branch.add("🔗 Link")
            link_branch.add(result.get("link"))

    print(results_tree)


def get_parser():
    """Returns ArgumentParser"""
    parser = ArgumentParser(description="DarkSearch API Client")
    parser.add_argument("query", help="search query")
    parser.add_argument("-p", "--page", type=int, help="page number")
    parser.add_argument("-n", "--pages", type=int, help="number of pages")
    parser.add_argument("-w", "--wait", type=int, help="wait between requests")
    parser.add_argument("-j", "--json", action="store_true", help="prints as json")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="prints verbose json"
    )
    return parser


def main():
    """Execute this command line."""
    parser = get_parser()
    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        exit(1)

    client = Client(timeout=10)

    response = client.search(
        args.query, page=args.page, pages=args.pages, wait=args.wait
    )

    if args.json:
        print_func = print
        if not args.verbose:
            print_func = pprint
        print_func(response)
    else:
        if not isinstance(response, list):
            response = [response]
        print_response(response)


if __name__ == "__main__":
    main()
