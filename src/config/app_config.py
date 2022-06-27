import os

# App configurations

config = {
    'db_config':
        {
            'root_user_name': os.getenv('ROOT_USER_NAME', 'root'),
            'root_password': os.getenv('ROOT_PASSWORD', 'rootpassword'),

        },
    'aircraft_db_config': {
            'db_name': 'aircraft_db',
            'user_name': os.getenv('AIRCRAFT_DB_USER_NAME', 'aircraft_admin'),
            'user_password': os.getenv('AIRCRAFT_DB_PASSOWRD', 'arango'),
    }
}