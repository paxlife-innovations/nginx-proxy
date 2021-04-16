dockergen_http: docker-gen -watch -notify "nginx -s reload" /app/nginx_http.tmpl /etc/nginx/conf.d/http.conf
dockergen_https: docker-gen -watch -notify "nginx -s reload" /app/nginx_https.tmpl /etc/nginx/conf.d/https.conf
nginx: nginx
