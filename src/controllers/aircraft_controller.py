from core.db.aircraft_app_db import aircraft_db
from model.aircraft_model import aircraft_collection
from scripts.populate_aircraft_db import populate_aircraft_database


def filter_aircraft_by_field(field: str, value: str):
    return list(aircraft_collection.find({field: value}))


def filter_aircraft_array_field_contains(field: str, value: str):
    qry = "FOR doc IN aircraft FILTER '{value}' IN doc.{field} RETURN doc".format(value=value, field=field)
    return list(aircraft_db.aql.execute(qry))


def populate_aircraft_db():
    return populate_aircraft_database('input/Aircraft_Database-Sheet1.csv')
