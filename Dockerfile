# syntax=docker/dockerfile:1
FROM python:3.7
COPY . .
WORKDIR /
RUN pip install pipenv
#RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN pipenv install
EXPOSE 8000
WORKDIR /src
CMD ["pipenv", "run", "python","aircraft_app.py"]