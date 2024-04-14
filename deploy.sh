#!/bin/sh
docker build -t saadiabouloudene/django_bank ./web/.
docker push saadiabouloudene/django_bank

docker build -t saadiabouloudene/fastapi ./api/.
docker push saadiabouloudene/fastapi

az container create --resource-group RG_BOULOUDENES --file deploy.yaml