from config.dbconfig import pg_config
import psycopg2
class CollectionCenterDAO:

    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCenters(self):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByZip(self, zip):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where zipCode = %s;"
        cursor.execute(query, (zip,))
        result = cursor.fetchone()
        return result

    def getCenterByStreet(self, street):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where street = %s;"
        cursor.execute(query, (street,))
        result = cursor.fetchone()
        return result

    def getCenterByTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where town = %s;"
        cursor.execute(query, (town,))
        result = cursor.fetchone()
        return result

    def getCenterByState(self, state):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where state_region = %s;"
        cursor.execute(query, (state,))
        result = cursor.fetchone()
        return result

    def getCenterByCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where country = %s;"
        cursor.execute(query, (country,))
        result = cursor.fetchone()
        return result

    def getCenterByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where collection_center_name = %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result