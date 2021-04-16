#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -t web $DIR/web
docker build -t web-https $DIR/web-https
