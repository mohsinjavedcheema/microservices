#/bin/bash
docker rm frontend-node
docker build -t mohsinjavedcheema/frontend-node .
docker run -d --name frontend-node --network mynetwork -p 9090:9090 mohsinjavedcheema/frontend-node