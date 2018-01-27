from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):

        connection_url = "host=%s dbname=%s user=%s password=%s port=%s" % (pg_config['host'], pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from (select gastypeid as name,resourceid from fuel " \
                "UNION select foodtype as name,resourceid from food " \
                "UNION select watertype as name,resourceid from water " \
                "UNION select icebrand as name,resourceid from ice " \
                "UNION select clothingtype as name,resourceid from clothing " \
                "UNION select medicaldevicetype as name,resourceid from medicaldevices " \
                "UNION select heavyequipmenttype as name,resourceid from heavyequipment " \
                "UNION select tooltype as name,resourceid from tools " \
                "UNION select powergeneratortype as name,resourceid from powergenerator " \
                "UNION select batterytype as name,resourceid from batteries " \
                "UNION select medicinetype as name,resourceid from medicine) as product " \
                "natural inner join resources as r order by resourcetype"
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

    def getResourceType(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceType from resources where resourceID = %s;"
        cursor.execute(query, (rid,))
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
    ############################################################
    ####            Insert individual Resources             ####
    ############################################################

    def insertWater(self, resID, waterType, waterBrand, qtyMeasure):
        cursor = self.conn.cursor()
        query = "insert into water(resID, waterType, waterBrand, qtyMeasure) values (%s, %s, %s, %s) returning waterID;"
        cursor.execute(query, (resID, waterType, waterBrand, qtyMeasure))
        waterID = cursor.fetchone()[0]
        self.conn.commit()
        return waterID

    def insertFood(self, resID, foodTypeID, foodName, qtyWeight):
        cursor = self.conn.cursor()
        query = "insert into food(resID, foodTypeID, foodName, qtyWeight) values (%s, %s, %s, %s) returning foodID;"
        cursor.execute(query, (resID, foodTypeID, foodName, qtyWeight))
        foodID = cursor.fetchone()[0]
        self.conn.commit()
        return foodID

    def insertIce(self, resID, iceBrand, qtyWeight):
        cursor = self.conn.cursor()
        query = "insert into ice(resID, iceBrand, qtyWeight) values (%s, %s, %s) returning iceID;"
        cursor.execute(query, (iceBrand, qtyWeight))
        iceID = cursor.fetchone()[0]
        self.conn.commit()
        return iceID

    def insertClothing(self, resID, clothingType, clothing_size):
        cursor = self.conn.cursor()
        query = "insert into clothing(resID, clothingType, clothing_size) values (%s, %s, %s) returning clothingID;"
        cursor.execute(query, (resID, clothingType, clothing_size))
        clothingID = cursor.fetchone()[0]
        self.conn.commit()
        return clothingID

    def insertGas(self, resID, gasTypeID, gasBrand, gasOctanage, qty):
        cursor = self.conn.cursor()
        query = "insert into gas(resID, gasTypeID, gasBrand, gasOctanage, qty) values (%s, %s, %s, %s, %s) returning gasID;"
        cursor.execute(query, (resID, gasTypeID, gasBrand, gasOctanage, qty))
        gasID = cursor.fetchone()[0]
        self.conn.commit()
        return gasID

    def insertMedical(self, resID, medicalDeviceType, medDevName, medDevManufacturer, toTreat, qty):
        cursor = self.conn.cursor()
        query = "insert into medicalDevices(resID, medicalDeviceType, medDevName, medDevManufacturer, toTreat, qty) values (%s, %s, %s, %s, %s, %s) returning medicalDevicesID;"
        cursor.execute(query, (resID, medicalDeviceType, medDevName, medDevManufacturer, toTreat, qty))
        medicalDevicesID = cursor.fetchone()[0]
        self.conn.commit()
        return medicalDevicesID

    def insertHeavy(self, resID, heavyEquipmentType, heavyEquipmentBrand):
        cursor = self.conn.cursor()
        query = "insert into heavyEquipment(resID, heavyEquipmentType, heavyEquipmentBrand) values (%s, %s, %s) returning heavyEquipmentID;"
        cursor.execute(query, (resID, heavyEquipmentType, heavyEquipmentBrand))
        heavyEquipmentID = cursor.fetchone()[0]
        self.conn.commit()
        return heavyEquipmentID

    def insertTools(self, resID, toolType, toolBrand, qty):
        cursor = self.conn.cursor()
        query = "insert into tools(resID, toolType, toolBrand, qty) values (%s, %s, %s, %s) returning toolsID;"
        cursor.execute(query, (resID, toolType, toolBrand, qty))
        toolsID = cursor.fetchone()[0]
        self.conn.commit()
        return toolsID

    def insertPower(self, resID, powerGeneratorType, powerGeneratorBrand, watts, qty):
        cursor = self.conn.cursor()
        query = "insert into powerGenerator(resID, powerGeneratorType, powerGeneratorBrand, watts, qty) values (%s, %s, %s, %s, %s) returning powerGeneratorID;"
        cursor.execute(query, (resID, powerGeneratorType, powerGeneratorBrand, watts, qty))
        powerGeneratorID = cursor.fetchone()[0]
        self.conn.commit()
        return powerGeneratorID

    def insertBatteries(self, resID, batteryType, batteryBrand, batteryVoltage, qty):
        cursor = self.conn.cursor()
        query = "insert into batteries(resID, batteryType, batteryBrand, batteryVoltage, qty) values (%s, %s, %s, %s, %s) returning batteriesID;"
        cursor.execute(query, (resID, batteryType, batteryBrand, batteryVoltage, qty))
        batteriesID = cursor.fetchone()[0]
        self.conn.commit()
        return batteriesID

    def insertMedicine(self, resID, medicineType, medicine_form, medicine_name, medicine_exp_date, medicine_manufacturer, v):
        cursor = self.conn.cursor()
        query = "insert into medicine(resID, medicineType, medicine_form, medicine_name, medicine_exp_date, medicine_manufacturer, v) values (%s, %s, %s, %s, %s, %s, %s) returning medicineID;"
        cursor.execute(query, (resID, medicineType, medicine_form, medicine_name, medicine_exp_date, medicine_manufacturer, v))
        medicineID = cursor.fetchone()[0]
        self.conn.commit()
        return medicineID

    def insertResource(self, resID, collectionCenterID, resourceType, buy_free, market_price, qty):
        cursor = self.conn.cursor()
        query = "insert into resources(resID, collectionCenterID, resourceType, buy_free, market_price, qty) values (%s, %s, %s, %s, %s, %s) return resourceID"
        cursor.execute(query, (resID, collectionCenterID, resourceType, buy_free, market_price, qty))
        resourceID = cursor.fetchone()[0]
        self.conn.commit()
        return resourceID
    
    ############################################################
    ####            Delete individual Resources             ####
    ############################################################

    def deleteWater(self, waterID):
        cursor = self.conn.cursor()
        query = "delete from water where resourceID = %s;"
        cursor.execute(query, (waterID,))
        self.conn.commit()
        return waterID

    def deleteFood(self, foodID):
        cursor = self.conn.cursor()
        query = "delete from food where resourceID = %s;"
        cursor.execute(query, (foodID,))
        self.conn.commit()
        return foodID

    def deleteIce(self, iceID):
        cursor = self.conn.cursor()
        query = "delete from ice where resourceID = %s;"
        cursor.execute(query, (iceID,))
        self.conn.commit()
        return iceID

    def deleteClothing(self, clothingID):
        cursor = self.conn.cursor()
        query = "delete from clothing where resourceID = %s;"
        cursor.execute(query, (clothingID,))
        self.conn.commit()
        return clothingID

    def deleteGas(self, gasID):
        cursor = self.conn.cursor()
        query = "delete from gas where resourceID = %s;"
        cursor.execute(query, (gasID,))
        self.conn.commit()
        return gasID

    def deleteMedical(self, medicalDevicesID):
        cursor = self.conn.cursor()
        query = "delete from medicalDevices where resourceID = %s;"
        cursor.execute(query, (medicalDevicesID,))
        self.conn.commit()
        return medicalDevicesID

    def deleteHeavy(self, heavyEquipmentID):
        cursor = self.conn.cursor()
        query = "delete from heavyEquipment where resourceID = %s;"
        cursor.execute(query, (heavyEquipmentID,))
        self.conn.commit()
        return heavyEquipmentID

    def deleteTools(self, toolsID):
        cursor = self.conn.cursor()
        query = "delete from tools where resourceID = %s;"
        cursor.execute(query, (toolsID,))
        self.conn.commit()
        return toolsID

    def deletePower(self, powerGeneratorID):
        cursor = self.conn.cursor()
        query = "delete from powerGenerator where resourceID = %s;"
        cursor.execute(query, (powerGeneratorID,))
        self.conn.commit()
        return powerGeneratorID

    def deleteBatteries(self, batteriesID):
        cursor = self.conn.cursor()
        query = "delete from batteries where resourceID = %s;"
        cursor.execute(query, (batteriesID,))
        self.conn.commit()
        return batteriesID

    def deleteMedicine(self, medicineID):
        cursor = self.conn.cursor()
        query = "delete from medicine where resourceID = %s;"
        cursor.execute(query, (medicineID,))
        self.conn.commit()
        return medicineID

    def deleteResource(self, resourceID, type):
        cursor = self.conn.cursor()
        query = "delete from resources where resourceID = %s;"
        cursor.execute(query, (resourceID,))
        self.conn.commit()
        if(type == "water"):
            removed = self.deleteWater(resourceID)
        elif (type == "food"):
            removed = self.deleteFood(resourceID)
        elif (type == "ice"):
            removed = self.deleteIce(resourceID)
        elif (type == "clothing"):
            removed = self.deleteClothing(resourceID)
        elif (type == "gas"):
            removed = self.deleteGas(resourceID)
        elif (type == "medicalDevices"):
            removed = self.deleteMedical(resourceID)
        elif (type == "heavyEquipment"):
            removed = self.deleteHeavy(resourceID)
        elif (type == "tools"):
            removed = self.deleteTools(resourceID)
        elif (type == "powerGenerator"):
            removed = self.deletePower(resourceID)
        elif (type == "batteries"):
            removed = self.deleteBatteries(resourceID)
        elif (type == "medicicne"):
            removed = self.deleteMedicine(resourceID)
        return resourceID

    ############################################################
    ####            Update individual Resources             ####
    ############################################################

    #TODO: FIGURE OUT THE UPDATES OF THESE RESOURCES

    def updateWater(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateFood(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateIce(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateClothing(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateGas(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateMedical(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateHeavy(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateTools(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updatePower(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateBatteries(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID

    def updateMedicine(self, collectionCenterID, collection_center_name, street, town, state_region, country, zipCode):
        cursor = self.conn.cursor()
        query = "update collectionCenter set collection = %s,_center_name = %s, street = %s, town = %s, state_region = %s, country = %s, zipCode = %s where collectionCenterID = %s;"
        cursor.execute(query, (collection_center_name, street, town, state_region, country, zipCode, collectionCenterID,))
        self.conn.commit()
        return collectionCenterID
