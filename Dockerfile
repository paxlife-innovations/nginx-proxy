FROM nginx:1.19.3
LABEL maintainer="Jason Wilder mail@jasonwilder.com"

# Install wget and install/updates certificates
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends ca-certificates wget jq \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*


# Configure Nginx
COPY ./system-nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/*.conf

# Install Forego
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego

ENV DOCKER_GEN_VERSION 0.7.4

RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

COPY ./system-nginx/network_internal.conf /etc/nginx/

COPY ./system-nginx/* /app/
WORKDIR /app/

ENV DOCKER_HOST unix:///tmp/docker.sock

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["forego", "start", "-r"]
