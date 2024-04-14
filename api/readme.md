pour construire l'image docker:
docker build . -t api:0.0.1

pour lancer sur le port 8000 en l'appelant 'api' (--name api):
docker run -p 8000:8000 --name api api:0.0.1

pour aller voir dans le conteneur 'api' (en lançant bash):
docker exec -it api bash