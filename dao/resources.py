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
        query = "select * from resources where resourceid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByCollectionCenterID(self, ccid):
        cursor = self.conn.cursor()
        query = "select * from resources where collectionCenterid = %s;"
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

    def getResourceInfoByName(self, rname):
        cursor = self.conn.cursor()
        query = "select id, resourceid, r.resourcetype, name, brand, r.market_price, r.qty, r.buy_free  " \
                "from(select gasid as id, resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name, foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid, watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id, resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r " \
                "where LOWER(r.resourcetype)=LOWER(%s);"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceInfoByType(self, rtype):
        cursor = self.conn.cursor()
        query = "select id, resourceid, r.resourcetype, name, brand, r.market_price, r.qty, r.buy_free  " \
                "from(select gasid as id, resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name, foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid, watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id, resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r " \
                "where LOWER(products.name)=LOWER(%s);"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceInfoByBF(self, buy_free):
        cursor = self.conn.cursor()
        query = "select id, resourceid, r.resourcetype, name, brand, r.market_price, r.qty, r.buy_free  " \
                "from(select gasid as id, resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name, foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid, watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id, resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r " \
                "where r.buy_free= %s;"
        cursor.execute(query, (buy_free,))
        result = []
        for row in cursor:
            result.append(row)
        return result
