import logging

from config.app_config import config
from core.db.arango_db import ArangoDBConnection

# Functions related to the Aircraft Database management

def get_db_connection():
    """
    Get the system database connection
    :return:
    """
    db_conf = config.get('db_config', {})
    return ArangoDBConnection(db_conf)


def get_create_aircraft_db(connection):
    """
    Get or Create the aircraft Database (if does not exists)

    :param connection:
    :return:
    """
    aircraft_db_conf = config.get('aircraft_db_config', {})
    if not connection.has_database(aircraft_db_conf.get('db_name')):
        return connection.get_db(**aircraft_db_conf)
    else:
        return connection.create_db(**aircraft_db_conf)


db_connection = get_db_connection()
aircraft_db = get_create_aircraft_db(db_connection)
