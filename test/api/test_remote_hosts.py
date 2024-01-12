from unittest.mock import patch

from remote_etc_hosts import RemoteHosts


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA")
def test_ip_domain(mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    assert ins.ip_domains.get("192.168.0.1") == {"dnsA"}


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA")
def test_domain_ip(mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    assert ins.domain_ip.get("dnsA") == "192.168.0.1"


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA")
def test_query_ip_by_domain(mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    assert ins.query_ip_by_domain("dnsA") == "192.168.0.1"


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA")
def test_query_domain_by_ip(mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    assert ins.query_domains_by_ip("192.168.0.1") == {"dnsA"}


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA")
@patch.object(RemoteHosts, "_write_to_hosts", return_value=print)
def test_add_item(mock_write_to_hosts, mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    ins._write_to_hosts = mock_write_to_hosts()
    ins.add_item("10.0.0.2", {"dnsC"})
    assert ins.query_domains_by_ip("10.0.0.2") == {"dnsC"}
    assert ins.query_ip_by_domain("dnsC") == "10.0.0.2"


@patch.object(
    RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA\n192.168.0.2 dnsB"
)
@patch.object(RemoteHosts, "_write_to_hosts", return_value=print)
def test_delete_item_by_ip(mock_write_to_hosts, mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    ins._write_to_hosts = mock_write_to_hosts()
    ins.delete_item_by_ip("192.168.0.1")
    assert ins.ip_domains.get("192.168.0.1") is None
    assert ins.ip_domains.get("192.168.0.2") == {"dnsB"}


@patch.object(RemoteHosts, "raw_hosts", return_value="192.168.0.1 dnsA dnsB")
@patch.object(RemoteHosts, "_write_to_hosts", return_value=print)
def test_delete_item_by_domain(mock_write_to_hosts, mock_raw_hosts):
    ins = RemoteHosts(ip="10.0.0.1", username="root", password="password")
    ins.raw_hosts = mock_raw_hosts()
    ins._write_to_hosts = mock_write_to_hosts()
    ins.delete_item_by_domain("dnsA")
    assert ins.ip_domains.get("192.168.0.1") == {"dnsB"}
