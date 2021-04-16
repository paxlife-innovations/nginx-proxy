import pytest
from requests import ConnectionError


def test_unknown_virtual_host_is_503(docker_compose, nginxproxy):
    with pytest.raises(ConnectionError):
        nginxproxy.get("https://unknown.nginx-proxy.tld")


def test_webA_is_forwarded(docker_compose, nginxproxy):
    web_container = docker_compose.containers.get("web")
    r = nginxproxy.get("https://webA.nginx-proxy.tld", verify=False)
    assert r.status_code == 200
    assert "I\'m %s" % web_container.id[:12] == r.text


def test_webB_is_forwarded(docker_compose, nginxproxy):
    web_container = docker_compose.containers.get("web")
    r = nginxproxy.get("https://webB.nginx-proxy.tld", verify=False)
    assert r.status_code == 200
    assert "I\'m %s" % web_container.id[:12] == r.text
