from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where resourceID = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceByCollectionCenterID(self, ccid):
        cursor = self.conn.cursor()
        query = "select * from resources where collectionCenterID = %s;"
        cursor.execute(query, (ccid,))
        result = cursor.fetchone()
        return result

    def getResourceByResourceTypeID(self, rtid):
        cursor = self.conn.cursor()
        query = "select * from resources where resourceTypeID = %s;"
        cursor.execute(query, (rtid,))
        result = cursor.fetchone()
        return result

    def getResourceByPurchasedFree(self, rfree):
        cursor = self.conn.cursor()
        query = "select * from resources where purchased_free = %s;"
        cursor.execute(query, (rfree,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByResourcePrice(self, rprice):
        cursor = self.conn.cursor()
        query = "select * from resources where resource_price = %s;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByQty(self, rqty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty = %s;"
        cursor.execute(query, (rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result