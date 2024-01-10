import pytest

from remote_etc_hosts.exceptions import EmptyHosts
from remote_etc_hosts.utils import parse_hosts


def test_parse_hosts():
    raw_hosts = """
127.0.0.1	localhost   localhost4
255.255.255.255	broadcasthost
    """
    handle_hosts = parse_hosts(raw_hosts)
    assert handle_hosts == [
        ("127.0.0.1", ["localhost", "localhost4"]),
        ("255.255.255.255", ["broadcasthost"])
    ]


def test_parse_hosts_empty_hosts():
    raw_hosts = ""
    with pytest.raises(EmptyHosts):
        parse_hosts(raw_hosts)
