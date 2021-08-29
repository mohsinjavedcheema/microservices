#/bin/bash
docker rm backend-python
docker build -t mohsinjavedcheema/backend-python .
docker run -d --name backend-python --network mynetwork -p 8080:8080 mohsinjavedcheema/backend-python