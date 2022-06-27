# Aircraft DB

## REQUIREMENTS/DEPENDENCIES:
* Running with Docker:  Docker 
* Running App Locally: Docker, pipenv

### Build Aircraft DB APP
* Go to the project root path /aircraftDB
* docker build -t aircraft_db --network=host .

### RUN ArangoDB Docker Container and Aircraft DB App in Docker Container
* Go to the project root path /aircraftDB
* run command:  docker-compose up
* To access the database browse to http://0.0.0.0:8529 and enter root username and password to login

###  RUN Aircraft DB App locally
* Go to the root folder and run
* pipenv install (if not already done)
* pipenv run python aircraft_app.py

## Run Queries:
* Using a browser or other tools you can access the following endpoints:
1) localhost:8000/populate_db: To populate the database with the inputs data
2) localhost:8000/filter_aircraft?field=...,value=...  Where field is the name of the field. The supported fields are
['Model', 'ATCT Weight Class', 'Tags']

## Architecture & Design:
* Using ArangoDB as database which supports NOSQL Document database, Graph Database and search database
* Modules:
  * config: Contain the configuration settings
  * controllers: Domain logic functions
  * core: Core components such as Database Connection
  * input: input files
  * model: Definition of the model collection
  * scripts: Scripts to execute such as populate_aircraft_db
  * test:  tests folder
  * aircraft_app.py:  Flask Application and Endpoints handlers
* Needs to be easily adapted to other databases. Used abstract classed to define the connection with the database. Use of flexible arguments to allow for flexibility.
