import pytest


def test_https_forwarding(docker_compose, nginxproxy):
    web1_container = docker_compose.containers.get("web1")
    r = nginxproxy.get("https://web1.nginx-proxy.tld", verify=False)
    assert r.status_code == 200
    assert "I\'m %s" % web1_container.id[:12] == r.text
