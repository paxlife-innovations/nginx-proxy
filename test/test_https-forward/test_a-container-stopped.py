import time

import pytest
from requests import ConnectionError


def test_nginx_proxy_still_running(docker_compose, nginxproxy):
    time.sleep(3)
    nginxproxy_container = docker_compose.containers.get("nginxproxy")
    web1_container = docker_compose.containers.get("web1")
    assert nginxproxy_container.status == "running"
    assert web1_container.status == "exited"
