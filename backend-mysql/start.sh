#/bin/bash
docker rm backend-mysql
docker network create mynetwork
docker build -t mohsinjavedcheema/backend-mysql .
docker run -d --name backend-mysql -v $(pwd)/dbdata:/var/lib/mysql --network mynetwork -p 3306:3306 mohsinjavedcheema/backend-mysql