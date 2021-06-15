import pytest


@pytest.mark.script_launch_mode("subprocess")
def test_help(script_runner):  # noqa: D103
    ret = script_runner.run("darksearch", "--help")
    assert ret.success
    assert "usage: darksearch" in ret.stdout
    assert ret.stderr == ""
