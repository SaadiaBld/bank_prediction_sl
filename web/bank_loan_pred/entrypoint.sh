#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "En attente de la disponibilité de Postgres..."
  sleep 1
done

# Effectuer les migrations
echo "Effectuer les migrations de la base de données..."
python bank_loan_pred/manage.py makemigrations && python manage.py migrate
python bank_loan_pred/manage.py runserver 0.0.0.0:8001