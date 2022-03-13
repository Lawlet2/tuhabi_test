import mysql.connector


class MySQLConnectionManager:
    """
    A class manager to handle the MySQL Connector/Python
    """
    def __init__(self, **db_config):
        """
        :param dict db_config: database configuration
        """
        self.db_config = db_config
        self.result = ()

    def __enter__(self):
        """
        called at start of with block to start the
        connection and cursor
        :return: self
        """
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor(buffered=False)
        except mysql.connector.Error as err:
            print("MySQL Connector Error:", err)
        else:
            return self

    def execute_query(self, query):
        """
        execute the query
        :param  str query: sql query
        :return:
        """
        self.cursor.execute(query)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        called at the end to close the connection
        """
        try:
            self.connection
        except AttributeError:
            pass
            print("No connection")
        else:
            self.connection.close()
