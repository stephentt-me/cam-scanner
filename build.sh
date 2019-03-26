#!/usr/bin/env bash
set -e

NOW=$(date +%s)
REGISTRY="asia.gcr.io/stephen-f52d1"

docker build -t ${REGISTRY}/cs-api:${NOW} api-python/
docker build -t ${REGISTRY}/cs-ip:${NOW} image-proccessing/

docker push ${REGISTRY}/cs-api:${NOW}
docker push ${REGISTRY}/cs-ip:${NOW}

figlet DONE
echo ${REGISTRY}/cs-api:${NOW}
echo ${REGISTRY}/cs-ip:${NOW}