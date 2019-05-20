import pytest


@pytest.mark.script_launch_mode("subprocess")
def test_help(script_runner):  # noqa: D103
    ret = script_runner.run("darksearch", "--help")
    assert (
        ret.stdout
        == """usage: darksearch [-h] [-q QUERY] [-p PAGE] [-n PAGES] [-w WAIT] [-j] [-v]

DarkSearch API Client

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        search query
  -p PAGE, --page PAGE  page number
  -n PAGES, --pages PAGES
                        number of pages
  -w WAIT, --wait WAIT  wait between requests
  -j, --json            prints as json
  -v, --verbose         prints verbose json
"""
    )
    assert ret.stderr == ""
