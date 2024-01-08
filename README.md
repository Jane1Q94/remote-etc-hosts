# remote-hosts

This is a simple tool for parsing `/etc/hosts` file in remote hosts.
Sure, It's very very simple but useful for someone need it. I just want to learn something from this wheel, :)

You can do these things if you install it.

1. get total view of /etc/hosts

```python
from remote_hosts import RemoteHosts
ins = RemoteHosts(ip="192.168.101.1", username="root", password="xxx")
print(dict(ins.ip_domains))
print(dict(ins.domain_ip))
```

2. query domain by ip

```python
print(ins.query_domains_by_ip("192.168.101.2"))
```

3. query ip by domain

```python
print(ins.query_ip_by_domain("domainA"))
```

4. add a new item to `/etc/hosts`

```python
ins.add_item("192.168.10.1", ["dnsA", "dnsB"])
print(dict(ins.domain_ip))
print(dict(ins.ip_domains))
```

5. del item by ip

```python
ins.delte_item_by_ip("192.168.10.1")
print(dict(ins.domain_ip))
print(dict(ins.ip_domains))
```

6. del item by domain

```python
ins.delete_item_by_domain("dnsB")
print(dict(ins.domain_ip))
print(dict(ins.ip_domains))
```

we also offer you some CLIs, such as:

# install
