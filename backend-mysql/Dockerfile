FROM mysql:5.7

LABEL name="Database Microservices" \   
     maintainer="Mohsin Javed Cheema <mohsinjavedcheema@gmail.com>" \
     summary="A Backend and Frontend Application"

ENV MYSQL_ROOT_PASSWORD=mysecret
ENV MYSQL_DATABASE=mydb

EXPOSE 3306

ADD dump.sql /docker-entrypoint-initdb.d