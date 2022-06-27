import csv
import logging
from model.aircraft_model import aircraft_collection, aircraft_schema

aircraft_schema_properties = aircraft_schema['rule']['properties']
fieldnames = aircraft_schema_properties.keys()


def data_hygiene(data_list):
    """
    Function to clean up and adapt the imported data, before saving it to the database
    :param data_list:
    :return:
    """

    def get_property_type(_property):
        """
        Get the schema property type
        :param _property:
        :return:
        """
        return aircraft_schema_properties.get(_property, {}).get('type')

    def map_undefined(value):
        """
        Change all the undefined values such as tbd  to undefined to avoid data inconsistency such as "tbd" in number
        field
        :param value:
        :return:
        """
        if value in ['tbd']:
            return None
        return value

    def map_type(_property, val):
        """
        Apply the data Property Type

        :param _property:
        :param val:
        :return:
        """
        _type = get_property_type(_property)
        try:
            if (val is None):
                return val
            if (_type == 'string'):
                return val
            elif (_type == 'number'):
                return float(val.replace(',', ''))
            elif (_type == 'boolean'):
                return bool(val)
            else:
                return val
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
    """
    Populate the database with the Aircraft Database Sheet csv input file
    :param csv_file_path:
    :return:
    """

    with open(csv_file_path, encoding='utf-8') as csvf:
        csv_data = csv.DictReader(csvf, fieldnames=fieldnames)
        data = data_hygiene(list(csv_data)[1:])
        response = aircraft_collection.insert_many(data)
        logging.info('populating DB')

    return response
