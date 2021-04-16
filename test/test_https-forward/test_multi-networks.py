import pytest
from requests import ConnectionError


def test_unknown_virtual_host(docker_compose, nginxproxy):
    with pytest.raises(ConnectionError):
        nginxproxy.get("https://nginx-proxy/")


def test_forwards_to_web1(docker_compose, nginxproxy):
    web1_container = docker_compose.containers.get("web1")
    r = nginxproxy.get("https://web1.nginx-proxy.local", verify=False)
    assert r.status_code == 200
    assert "I\'m %s" % web1_container.id[:12] == r.text


def test_forwards_to_web2(docker_compose, nginxproxy):
    web2_container = docker_compose.containers.get("web2")
    r = nginxproxy.get("https://web2.nginx-proxy.local", verify=False)
    assert r.status_code == 200
    assert "I\'m %s" % web2_container.id[:12] == r.text
