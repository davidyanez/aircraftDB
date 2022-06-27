from core.db.aircraft_app_db import aircraft_db

aircraft_schema = {
    'rule': {
        'type': 'object',
        'properties': {
            'Date Completed': {'type': 'string'},
            'Manufacturer': {'type': 'string'},
            'Model': {'type': 'string'},
            'Physical Class Engine': {'type': 'string'},
            '# Engines': {'type': 'number'},
            'AAC': {'type': 'string'},
            'ADG': {'type': 'string'},
            'TDG': {'type': 'string'},
            'Approach Speed Vref': {'type': 'number'},
            'Wingtip Configuration': {'type': 'string'},
            'Wingspan ft': {'type': 'number'},
            'Length ft': {'type': 'number'},
            'Tail Height ft OEW': {'type': 'number'},
            'Wheelbase, ft': {'type': 'number'},
            'Cockpit to Main Gear CMG': {'type': 'string'},
            'MGW Outer to Outer': {'type': 'number'},
            'MTOW': {'type': 'number'},
            'Max Ramp Max Taxi': {'type': 'number'},
            'Main Gear Config': {'type': 'string'},
            'ICAO Code': {'type': 'string'},
            'Wake Category': {'type': 'string'},
            'ATCT Weight Class': {'type': 'string'},
            'Years Manufactured': {'type': 'number'},
            'Note': {'type': 'string'},
            'Tags': {'type': 'array'},
        },
    },
    'level': 'none',
    'message': 'Schema Validation Failed.'
}


def get_create_aircraft_collection():
    """
    Get or create the aircraft collection

    :return:
    """

    collection_name = 'aircraft'
    if aircraft_db.has_collection(collection_name):
        return aircraft_db.collection(collection_name)
    else:
        return aircraft_db.create_collection(name=collection_name, schema=aircraft_schema)


# aircraft collection object
aircraft_collection = get_create_aircraft_collection()
