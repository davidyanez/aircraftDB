import csv
import logging
from model.aircraft_model import aircraft_collection, aircraft_schema

aircraft_schema_properties = aircraft_schema['rule']['properties']
fieldnames = aircraft_schema_properties.keys()


def data_hygiene(data_list):

    def get_property_type(_property):
        return aircraft_schema_properties.get(_property, {}).get('type')

    def map_undefined(value):
        if value in ['tbd']:
            return None
        return value

    def map_type(_property, value):
        _type = get_property_type(_property)
        try:
            if (value is None):
                return value
            if (_type == 'string'):
                return value
            elif (_type == 'number'):
                return float(value.replace(',',''))
            elif (_type == 'boolean'):
                return bool(value)
            else:
                return value
        except Exception as e:
            logging.error(str(e) + f'for property ${_property}')
            return None;

    for data in data_list:
        for _property in data.keys():
            property_type = get_property_type(_property)
            value = data[_property]
            value = map_undefined(value)
            value = map_type(_property, value)
            if property_type == 'array':
                value = value.split(',')
            data[_property] = value
    return data_list


def populate_aircraft_database(csv_file_path):
    with open(csv_file_path, encoding='utf-8') as csvf:
        csv_data = csv.DictReader(csvf, fieldnames=fieldnames)
        data = data_hygiene(list(csv_data)[1:])
        response = aircraft_collection.insert_many(data)
        logging.info('populating DB')

    return response