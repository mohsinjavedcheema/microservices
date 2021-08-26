FROM python:3.6-alpine

RUN pip install flask

# RUN pip install flask-mysqldb

# RUN pip install mysql-python

RUN pip install flask-mysql

COPY app.py /

# EXPOSE 8080

CMD [ "python", "./app.py" ]