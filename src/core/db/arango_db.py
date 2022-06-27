from arango import ArangoClient

from core.db.db_connection import DBConnection


class ArangoDBConnection(DBConnection):
    """
        This class Handles the Connection and system operations to ArangoDB
    """

    def __init__(self, conf):

        super().__init__(conf)
        self.client = ArangoClient()
        self.system_db = self.get_system_db()

    def get_db(self, **kwargs):
        """

        :param kwargs:
            db_name: The database name
            user_name: The database connection user name
            user_password: the database connection password
        :return: The Database
        """

        db_name = kwargs['db_name']
        user_name = kwargs['user_name']
        user_password = kwargs['user_password']
        if db_name and user_name and user_password:
            return self.client.db(db_name, username=user_name, password=user_password)
        else:
            raise Exception('Invalid parameters')

    def get_system_db(self):
        """
        Get the System database which is used for system operations
        :return:
        """
        return self.get_db(
            db_name='_system',
            user_name=self.config.get('root_user_name'),
            user_password=self.config.get('root_password'))

    def has_database(self, name):
        """
        Check if a database exists

        :param name: Database name
        :return: (boolean) database exists
        """
        return self.system_db.has_database(name)

    def create_db(self, **kwargs):
        """
        Create a database

        :param kwargs:
            db_name: the database name
            user_name: The database connection user name
            user_password: the database connection password
        :return: created database object
        """

        database_name = kwargs['db_name']
        if not self.system_db.has_database(database_name):
            return self.system_db.create_database(database_name)
        return self.get_db(**kwargs)

