from config.dbconfig import pg_config
import psycopg2
class LocationDAO:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllLocations(self):
        cursor = self.conn.cursor()
        query = "select * from location;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLocationByZip(self, zip):
        query = "select * from location where zipcode = %s;"
        cursor.execute(query, (zip,))
        result = cursor.fetchone()
        return result

    def getLocationByCountryID(self, cid):
        query = "select * from location where countryID = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getLocationByStateID(self, sid):
        query = "select * from location where state_regionID = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getLocationByTownID(self, tid):
        query = "select * from location where townID = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result