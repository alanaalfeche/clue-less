FROM python:alpine

EXPOSE 5000

ENV PYTHONPATH="$PYTHONPATH:/core"

RUN pip install attrs
RUN pip install flask
RUN pip install networkx
RUN pip install requests

# Full install of PostgreSQL python module
RUN apk update
RUN apk add postgresql-dev gcc musl-dev
RUN pip install psycopg2
