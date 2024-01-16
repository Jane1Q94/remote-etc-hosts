import os

import pytest

from remote_etc_hosts.cli import RemoteHostsCli


def test_parameter_from_env():
    os.environ["REMOTE_HOST_SSH_USER"] = "test_username"
    os.environ["REMOTE_HOST_SSH_PASSWORD"] = "test_password"
    cli = RemoteHostsCli("10.0.0.1")
    assert cli.username == "test_username"
    assert cli.password == "test_password"


def test_parameter_exception():
    del os.environ["REMOTE_HOST_SSH_USER"]
    del os.environ["REMOTE_HOST_SSH_PASSWORD"]
    with pytest.raises(AssertionError):
        RemoteHostsCli("10.0.0.1")
