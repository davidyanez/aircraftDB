# Aircraft DB

## REQUIREMENTS/DEPENDENCIES:
* Running with Docker:  Docker 
* Running App Locally: Docker, pipenv
* Code dependencies:  flask, waitress, python-arango, arangodb (database)

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
  * controllers: Handles the Domain logic functions, to be used by the endpoint handlers
  * core: Core components such as Database Connection
  * input: input files such as Aircraft_Database-Sheet1
  * model: Definition of the model collection
  * scripts: Scripts to execute such as populate_aircraft_db
  * test:  tests folder for all the project test cases
  * aircraft_app.py:  Flask Application and Endpoints handlers
* Needs to be easily adapted to other databases. Used abstract classed to define the connection with the database. Use of flexible arguments to allow for flexibility.
* We used field names as in the input csv file but eliminated the "(" ")" characters
* Populate DB import scripts assumes all expected data fields are in the correct order
* Endoints:
  * filter_aircraft: Find aircraft items by Model, Weight Class and Tags.
  * populate_db: Import the csv data file into the database. 