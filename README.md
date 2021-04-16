# Nginx proxy

The nginx proxy component acts as a `router` to route request to the correct container depend on domain name in the request. The system nginx is `transparent` when looking from client side. It simply forwards the request from client to the specified container.
The code here is customized from repository https://github.com/nginx-proxy/nginx-proxy/

## Usage
To register domain name with system nginx (all requests to some specific domain will be routed to the container), user need to set environment following variables of the container:
* VIRTUAL_HOST: keep the value of domain name that the container serves. For example VIRTUAL_HOST=foo.com. In case the container is responsible for multiple domains, user only need to separate them by commas. For example VIRTUAL_HOST=foo.com,bar.com,foo.bar.com.
* VIRTUAL_PORT: value of which port of container receives traffic from system nginx. If the container exposes multiple ports, system nginx will forward traffic to port 80 by default. If user needs to specify a different port, he/she can set a VIRTUAL_PORT env var to select a different one. If the container only exposes one port (specified in Dockerfile when build image) and it has a VIRTUAL_HOST env var set, that port will be selected.
* VIRTUAL_PROTO: when the container serves https only, user should provide this environment variable value `https` so that the request is correctly forward to that container.

## Test

To test the functionalities of nginx proxy please run:
```sh
make test
```
