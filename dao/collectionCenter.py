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

    def getCenterByID(self, ccid):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter where collectionCenterID = %s;"
        cursor.execute(query, (ccid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from collectionCenter as cc, " \
                "resources as r where cc.collectioncenterid = r.collectioncenterid" \
                " and LOWER(r.resourcetype) = LOWER(%s);"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceType(self, rtype):
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

        cursor.execute(query, (rtype,))
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

        cursor.execute(query, (rtype, town))
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

        cursor.execute(query, (rtype, state))
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

        cursor.execute(query, (rtype, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourceTypeAndCenterName(self, rtype, ccname):
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

    def getCenterByResourcesAvailableAndCenterName(self, ccname):
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
        cursor.execute(query, (ccname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndCountry(self, country):
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
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndState(self, state):
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
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByResourcesAvailableAndTown(self, town):
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

        cursor.execute(query, (town,))
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

    ##=================================FUEL=========================================================================##
    def getCenterByFuelType(self, ftype):
        cursor = self.conn.cursor()
        query = "select * from (select gasid as id, resourceid, gastypeid as name, gasbrand as brand, gasoctanage from fuel)" \
                " as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s)"
        cursor.execute(query, (ftype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFuelTypeAndTown(self, ftype, town):
        cursor = self.conn.cursor()
        query = "select * from (select gasid as id, resourceid, gastypeid as name, gasbrand as brand, gasoctanage from fuel)" \
                " as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.town) = LOWER(%s)"
        cursor.execute(query, (ftype, town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFuelTypeAndCountry(self, ftype, country):
        cursor = self.conn.cursor()
        query = "select * from (select gasid as id, resourceid, gastypeid as name, gasbrand as brand, gasoctanage from fuel)" \
                " as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.country) = LOWER(%s)"
        cursor.execute(query, (ftype, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFuelTypeAndState(self, ftype, state):
        cursor = self.conn.cursor()
        query = "select * from (select gasid as id, resourceid, gastypeid as name, gasbrand as brand, gasoctanage from fuel)" \
                " as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.state_region) = LOWER(%s)"
        cursor.execute(query, (ftype, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##===============================================================================================================##

    ##=================================WATER=========================================================================##
    def getCenterByWater(self):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town) = LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country) = LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.region_state) = LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterType(self, wtype):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(w.name)=LOWER(%s)"
        cursor.execute(query, (wtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterTypeAndTown(self, wtype, town):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(w.name) = LOWER(%s) and LOWER(cc.town) = LOWER(%s)"
        cursor.execute(query, (wtype, town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterTypeAndCountry(self, wtype, country):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(w.name) = LOWER(%s) and LOWER(cc.country) = LOWER(%s)"
        cursor.execute(query, (wtype, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByWaterTypeAndState(self, wtype, state):
        cursor = self.conn.cursor()
        query = "select * from(select waterid as id, resourceid, watertype as name, waterbrand as brand, qtymeasure from water) " \
                "as w natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(w.name) = LOWER(%s) and LOWER(cc.region_state) = LOWER(%s)"
        cursor.execute(query, (wtype, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##===============================================================================================================##

    # FOOD

    def getCenterByFood(self):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region) = LOWER(%s) "
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country) = LOWER(%s) "
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town) = LOWER(%s) "
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodType(self, rtype):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) "
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodTypeAndCountry(self, rtype, country):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (rtype, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodTypeAndState(self, rtype, state):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (rtype, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByFoodTypeAndTown(self, rtype, town):
        cursor = self.conn.cursor()
        query = "select * from (select foodid as id, resourceid, foodtype as name, foodName as brand, qtyweight  " \
                "from food ) as f natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(f.name) = LOWER(%s) and LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (rtype, town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##==============================================================================================================##
    # MEDICAL DEVICES
    def getCenterByMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select * from(select medicaldevicesid as id, resourceid, medicaldevicetype as name, " \
                "meddevname as brand, meddevmanufacturer, totreat from medicaldevices ) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicalDeviceAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from(select medicaldevicesid as id, resourceid, medicaldevicetype as name, " \
                "meddevname as brand, meddevmanufacturer, totreat from medicaldevices ) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town)=LOWER(%s) "
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicalDeviceAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from(select medicaldevicesid as id, resourceid, medicaldevicetype as name, " \
                "meddevname as brand, meddevmanufacturer, totreat from medicaldevices ) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region)=LOWER(%s) "
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicalDeviceAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from(select medicaldevicesid as id, resourceid, medicaldevicetype as name, " \
                "meddevname as brand, meddevmanufacturer, totreat from medicaldevices ) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country)=LOWER(%s) "
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##================================================================================================================##

    def getCenterByMedicine(self):
        cursor = self.conn.cursor()
        query = "select * from (select medicineid as id, resourceid, medicinetype as name, medicine_name as brand," \
                " medicine_form, medicine_manufacturer from medicine) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicineAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select medicineid as id, resourceid, medicinetype as name, medicine_name as brand," \
                " medicine_form, medicine_manufacturer from medicine) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicineAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select medicineid as id, resourceid, medicinetype as name, medicine_name as brand," \
                " medicine_form, medicine_manufacturer from medicine) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByMedicineAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select medicineid as id, resourceid, medicinetype as name, medicine_name as brand," \
                " medicine_form, medicine_manufacturer from medicine) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##===============================================================================================================##

    ##HEAVY EQUIPMENT
    def getCenterByHeavyEquipment(self):
        cursor = self.conn.cursor()
        query = "select * from (select heavyequipmentid as id, resourceid, heavyequipmenttype as name, " \
                "heavyequipmentbrand as brand from heavyequipment) as m " \
                "natural inner join resources as r natural inner join collectioncenter as cc"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByHeavyEquipmentAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select heavyequipmentid as id, resourceid, heavyequipmenttype as name, " \
                "heavyequipmentbrand as brand from heavyequipment) as h " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town)= LOWER(%s)"

        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByHeavyEquipmentAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select heavyequipmentid as id, resourceid, heavyequipmenttype as name, " \
                "heavyequipmentbrand as brand from heavyequipment) as h " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region)= LOWER(%s)"

        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByHeavyEquipmentAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select heavyequipmentid as id, resourceid, heavyequipmenttype as name, " \
                "heavyequipmentbrand as brand from heavyequipment) as h " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country)= LOWER(%s)"

        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##================================================================================================================##

    def getCenterByPowerGenerator(self):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town) = LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region) = LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country) = LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndWatts(self, watts):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where p.watts = %s"
        cursor.execute(query, (watts,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndWattsAndTown(self, watts, town):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where p.watts = %s and LOWER(cc.town)= LOWER(%s)"
        cursor.execute(query, (watts, town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndWattsAndState(self, watts, state):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where p.watts = %s and LOWER(cc.state_region)= LOWER(%s)"
        cursor.execute(query, (watts, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByPowerGeneratorAndWattsAndCountry(self, watts, country):
        cursor = self.conn.cursor()
        query = "select * from (select powergeneratorid as id, resourceid, powergeneratortype as name, " \
                "powergeneratorbrand as brand, watts from powergenerator) as p  " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where p.watts = %s and LOWER(cc.country)= LOWER(%s)"
        cursor.execute(query, (watts, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ##================================================================================================================##

    ##CLOTHING
    def getCenterByClothing(self):
        cursor = self.conn.cursor()
        query = "select * from (select clothingid as id, resourceid, clothingtype as name, " \
                "clothingbrand as brand, clothingcolor,clothing_size  from clothing) as c " \
                "natural inner join resources as r natural inner join collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByClothingAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select clothingid as id, resourceid, clothingtype as name, " \
                "clothingbrand as brand, clothingcolor,clothing_size  from clothing) as c " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByClothingAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select clothingid as id, resourceid, clothingtype as name, " \
                "clothingbrand as brand, clothingcolor,clothing_size  from clothing) as c " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByClothingAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select clothingid as id, resourceid, clothingtype as name, " \
                "clothingbrand as brand, clothingcolor,clothing_size  from clothing) as c " \
                "natural inner join resources as r natural inner join collectioncenter as cc " \
                "where LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBattery(self):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndBVoltage(self, bvoltage):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where b.batteryvoltage = %s"
        cursor.execute(query, (bvoltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndBVoltageAndTown(self, bvoltage, town):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where b.batteryvoltage = %s and LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (bvoltage, town))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndBVoltageAndState(self, bvoltage, state):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where b.batteryvoltage = %s and LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (bvoltage, state))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByBatteryAndBVoltageAndCountry(self, bvoltage, country):
        cursor = self.conn.cursor()
        query = "select * from (select batteriesid as id, resourceid, batterytype as name,  " \
                "batterybrand as brand, batteryvoltage from batteries) as b " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where b.batteryvoltage = %s and LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (bvoltage, country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByTools(self):
        cursor = self.conn.cursor()
        query = "select * from (select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools) as t" \
                " natural inner join resources as r natural inner join  collectioncenter as cc "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByToolsAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools) as t" \
                " natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.town)=LOWER(%s)"
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByToolsAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools) as t" \
                " natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.state_region)=LOWER(%s)"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByToolsAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select toolsid as id, resourceid, tooltype as name, toolbrand as brand from tools) as t" \
                " natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.country)=LOWER(%s)"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByIce(self):
        cursor = self.conn.cursor()
        query = "select * from (select iceid as id, resourceid, icebrand as name from ice) as i " \
                "natural inner join resources as r natural inner join  collectioncenter as cc  "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByIceAndTown(self, town):
        cursor = self.conn.cursor()
        query = "select * from (select iceid as id, resourceid, icebrand as name from ice) as i " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.town) = LOWER(%s) "
        cursor.execute(query, (town,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByIceAndState(self, state):
        cursor = self.conn.cursor()
        query = "select * from (select iceid as id, resourceid, icebrand as name from ice) as i " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.state_region) = LOWER(%s) "
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCenterByIceAndCountry(self, country):
        cursor = self.conn.cursor()
        query = "select * from (select iceid as id, resourceid, icebrand as name from ice) as i " \
                "natural inner join resources as r natural inner join  collectioncenter as cc " \
                "where LOWER(cc.country) = LOWER(%s) "
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailablebyCenter(self, ccname):
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
                "where r.qty>0 and LOWER(cc.collection_center_name) = LOWER(%s)"
        cursor.execute(query, (ccname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementResources(self):
        cursor = self.conn.cursor()
        query = "select resourcetype,qty,collection_center_name,town,state_region,country " \
                "from resources as r natural inner join collectioncenter as cc " \
                "where r.qty>0 " \
                "order by resourcetype"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "insert into collectionCenter(collection_center_name, street, town, state_region, country, zipCode) values (%s, %s, %s, %s, %s, %s) returning collectionCenterID;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode))
        collectionCenterID = cursor.fetchone()[0]
        self.conn.commit()
        return collectionCenterID

    def delete(self, ccid):
        cursor = self.conn.cursor()
        query = "delete from collectionCenter where collectionCenterID = %s;"
        cursor.execute(query, (ccid,))
        self.conn.commit()
        return ccid

    def update(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID
    
