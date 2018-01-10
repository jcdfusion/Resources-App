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
        query = "select * from collectionCenter where LOWER(street) = LOWER(%s);"
        cursor.execute(query, (street,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where LOWER(town) = LOWER(%s);"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByState(self, state):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where LOWER(state_region) = LOWER(%s);"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where LOWER(country) = LOWER(%s);"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where LOWER(collection_center_name) = LOWER(%s);"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceName(self,rname):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter as cc, " \
                "resources as r where cc.collectioncenterid = r.collectioncenterid" \
                " and LOWER(r.resourcetype) = LOWER(%s);"
        cursor.execute(query,(rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceType(self,rtype):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(name)=LOWER(%s);"

        cursor.execute(query,(rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceTypeAndTown(self, rtype, town):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(name)=LOWER(%s)" \
                "and LOWER(cc.town)=LOWER(%s);"

        cursor.execute(query, (rtype,town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceTypeAndState(self, rtype, state):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(name)=LOWER(%s)" \
                "and LOWER(cc.state_region)=LOWER(%s);"

        cursor.execute(query, (rtype,state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceTypeAndCountry(self, rtype, country):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(name)=LOWER(%s)" \
                "and LOWER(cc.country)=LOWER(%s);"

        cursor.execute(query, (rtype,country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceTypeAndCenterName(self,rtype,ccname):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(name)=LOWER(%s)" \
                "and LOWER(cc.collection_center_name)=LOWER(%s);"
        cursor.execute(query, (rtype, ccname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndCenterName(self,ccname):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0 " \
                "and LOWER(cc.ccname)=LOWER(%s)"
        cursor.execute(query,(ccname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndCountry(self,country):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0 " \
                "and LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query,(country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndState(self,state):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0 " \
                "and LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query,(state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndTown(self,town):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as products natural inner join resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0 " \
                "and LOWER(cc.town)=LOWER(%s)"

        cursor.execute(query,(town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersbyCCName(self, ccname):
        cursor = self.conn.cursor()
        query = "select * from(select gasid as id, " \
                "resourceid, gastypeid as name, gasbrand as brand " \
                "from fuel " \
                "UNION select foodid as id, resourceid, foodtype as name,foodName as brand " \
                "from food " \
                "UNION select waterid as id, resourceid,watertype as name, waterbrand as brand " \
                "from water " \
                "UNION select iceid as id,resourceid, icebrand as name, icebrand as brand " \
                "from ice " \
                "UNION select clothingid as id, resourceid, clothingtype as name, clothingbrand as brand " \
                "from clothing " \
                "UNION select medicaldevicesid as id, resourceid, medicaldevicetype as name, meddevname as brand " \
                "from medicaldevices " \
                "UNION select heavyequipmentid as id, resourceid, heavyequipmenttype as name, heavyequipmentbrand as brand " \
                "from heavyequipment " \
                "UNION select toolsid as id, resourceid, tooltype as name, toolbrand as brand " \
                "from tools " \
                "UNION select powergeneratorid as id, resourceid, powergeneratortype as name, powergeneratorbrand as brand " \
                "from powergenerator " \
                "UNION select batteriesid as id, resourceid, batterytype as name, batterybrand as brand " \
                "from batteries " \
                "UNION select medicineid as id, resourceid, medicinetype as name, medicine_name as brand " \
                "from medicine) as mega natural inner join resources as r  natural inner join purchases as pp " \
                "natural inner join collectioncenter as cc " \
                "where r.resourceid = pp.resourceid " \
                "and cc.collectioncenterid=pp.collectioncenterid " \
                "and LOWER(cc.collection_center_name)=LOWER(%s);"
        cursor.execute(query, (ccname,))
        result = []
        for row in cursor:
            result.append(row)
        return result








