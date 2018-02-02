from flask import jsonify
from dao.resources import ResourcesDAO
from dao.collectionCenter import CollectionCenterDAO


class ResourceHandler:

    def build_resources_dict(self, row):
        result = {}
        result['resourceid'] = row[0]  # resource id
        result['ccid'] = row[1]  # collection center id
        result['rname'] = row[2]  # resource name id
        result['buy_free'] = row[3]  # boolean whether the resource is free or not
        result['rprice'] = row[4]  # resource price
        result['qty'] = row[5]  # resource qty
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rname'] = row[0]  # resource type id
        return result

    def build_resourcetype_dict(self, row):
        result = {}
        result['rtid'] = row[0]  # resource type id
        result['rname'] = row[1]  # resource name
        return result

    def build_collectionCenter_dict(self, row):
        result = {}
        result['ccid'] = row[0]  # collection center id
        result['zipCode'] = row[1]  # zipCode
        result['street'] = row[2]  # street where collection center is located
        result['ccname'] = row[3]  # collection center name
        return result

    def build_resourcesInfo_dict(self, row):
        result = {}
        result['id'] = row[0]  # resource id
        result['resourceid'] = row[1]  # resource id
        result['rname'] = row[2]  # resource name id
        result['rtype'] = row[3]  # resource type
        result['rbrand'] = row[4]  # resource brand
        result['rprice'] = row[5]  # resource price
        result['qty'] = row[6]
        result['buy_free'] = row[7]
        return result

    def build_resourcesInf_dict(self, row):
        result = {}
        result['rid'] = row[0]  # resource id
        result['rtype'] = row[1]  # resource id
        result['ccid'] = row[2]  # resource name id
        result['rname'] = row[3]  # resource type
        result['buy_free'] = row[4]  # resource brand
        result['marketPrice'] = row[5]  # resource price
        result['qty'] = row[6]
        return result

    def build_resourcesInfoInsert_dict(self, row):
        result = {}
        result['resourceID'] = row[0]  # resource id
        result['collectionCenterID'] = row[1]  # resource id
        result['resourceType'] = row[2]  # resource name id
        result['buy_free'] = row[3]  # resource type
        result['market_price'] = row[4]  # resource brand
        result['qty'] = row[5]  # resource price
        return result

    def build_resourcesBySupplier_dict(self, row):
        result = {}
        result['resourceID'] = row[0]  # resource id
        result['collectionCenterID'] = row[1]  # resource id
        result['resourceType'] = row[2]  # resource name id
        result['buy_free'] = row[3]  # resource type
        result['market_price'] = row[4]  # resource brand
        result['qty'] = row[5]  # resource price
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResourcesInfo()
        result_list = []
        for row in resources_list:
            result = self.build_resourcesInf_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllResourcesInfo(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResourcesInfo()
        result_list = []
        for row in resources_list:
            result = self.build_resourcesInf_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, resourceID):
        dao = ResourcesDAO()
        resources_list = dao.getResourceById(resourceID)
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceBySupplier(self, collectionCenterID):
        dao = ResourcesDAO()
        resources_list = dao.getResourceByCollectionCenterID(collectionCenterID)
        result_list = []
        for row in resources_list:
            result = self.build_resourcesBySupplier_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def searchResources(self, args):
        rid = args.get('rid')
        rname = args.get('rname')
        rtype = args.get('rtype')
        buy_free = args.get('buy_free')
        ccid = args.get('ccid')
        marketprice = args.get('marketprice')
        qty = args.get('qty')

        dao = ResourcesDAO()

        if (len(args) == 1) and rid:
            resources_list = dao.getResourceById(rid)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)


        elif (len(args) == 1) and rname:
            resources_list = dao.getResourceInfoByName(rname)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif (len(args) == 1) and rtype:
            resources_list = dao.getResourceInfoByType(rtype)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif (len(args) == 1) and buy_free:
            resources_list = dao.getResourceInfoByBF(buy_free)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif (len(args) == 1) and ccid:
            resources_list = dao.getResourceByCollectionCenterID(ccid)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif (len(args) == 1) and marketprice:
            resources_list = dao.getResourceByMarketPrice(marketprice)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif (len(args) == 1) and qty:
            resources_list = dao.getResourceByQty(qty)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInf_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)


        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def insertResource(self, form):
        if form and len(form) < 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            collectionCenterID = form['collectionCenterID']
            resourceType = form['resourceType']
            buy_free = form['buy_free']
            market_price = form['market_price']
            resQty = form['qty']
            dao = ResourcesDAO()
            result = None
            daoCenter = CollectionCenterDAO()
            if not daoCenter.getCenterByID(collectionCenterID):
                return jsonify(Error="Center not found."), 404
            resID = dao.insertResource(collectionCenterID, resourceType, buy_free, market_price, resQty)
            if resourceType == 'water':
                waterType = form['waterType']
                waterBrand = form['waterBrand']
                if waterType and waterBrand and resQty:
                    dao.insertWater(resID, waterType, waterBrand, resQty)
            elif resourceType == 'food':
                foodTypeID = form['foodTypeID']
                foodName = form['foodName']
                if foodTypeID and foodName and resQty:
                    dao.insertFood(resID, foodTypeID, foodName, resQty)
            elif resourceType == 'ice':
                iceBrand = form['iceBrand']
                if iceBrand and resQty:
                    dao.insertIce(resID, iceBrand, resQty)
            elif resourceType == 'clothing':
                clothingType = form['clothingType']
                clothing_size = form['clothing_size']
                if clothingType and clothing_size and resQty:
                    dao.insertClothing(resID, clothingType, clothing_size, resQty)
            elif resourceType == 'gas':
                gasTypeID = form['gasTypeID']
                gasBrand = form['gasBrand']
                gasOctanage = form['gasOctanage']
                if gasTypeID and gasBrand and gasOctanage and resQty:
                    dao.insertGas(resID, gasTypeID, gasBrand, gasOctanage, resQty)
            elif resourceType == 'medicalDevices':
                medicalDeviceType = form['medicalDeviceType']
                medDevName = form['medDevName']
                medDevManufacturer = form['medDevManufacturer']
                toTreat = form['toTreat']
                if medicalDeviceType and medDevName and medDevManufacturer and toTreat and resQty:
                    dao.insertMedical(resID, medicalDeviceType, medDevName, medDevManufacturer, toTreat, resQty)
            elif resourceType == 'heavyEquipment':
                heavyEquipmentType = form['heavyEquipmentType']
                heavyEquipmentBrand = form['heavyEquipmentBrand']
                if heavyEquipmentType and heavyEquipmentBrand:
                    dao.insertHeavy(resID, heavyEquipmentType, heavyEquipmentBrand)
            elif resourceType == 'tools':
                toolType = form['toolType']
                toolBrand = form['toolBrand']
                if toolType and toolBrand and resQty:
                    dao.insertTools(resID, toolType, toolBrand, resQty)
            elif resourceType == 'powerGenerator':
                powerGeneratorType = form['powerGeneratorType']
                powerGeneratorBrand = form['powerGeneratorBrand']
                watts = form['watts']
                if powerGeneratorType and powerGeneratorBrand and watts and resQty:
                    dao.insertPower(resID, powerGeneratorType, powerGeneratorBrand, watts, resQty)
            elif resourceType == 'batteries':
                batteryType = form['batteryType']
                batteryBrand = form['batteryBrand']
                batteryVoltage = form['batteryVoltage']
                if batteryType and batteryBrand and batteryVoltage and resQty:
                    dao.insertBatteries(resID, batteryType, batteryBrand, batteryVoltage, resQty)
            elif resourceType == 'medicicne':
                medicineType = form['medicineType']
                medicine_form = form['medicine_form']
                medicine_name = form['medicine_name']
                medicine_exp_date = form['medicine_exp_date']
                medicine_manufacturer = form['medicine_manufacturer']
                if medicineType and medicine_form and medicine_name and medicine_exp_date and medicine_manufacturer and resQty:
                    dao.insertMedicine(resID, medicineType, medicine_form, medicine_name, medicine_exp_date, medicine_manufacturer, resQty)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
            #result = self.build_resourcesInf_dict(resID, collectionCenterID, resourceType, buy_free, market_price, resQty)
            #return jsonify(Resource=result), 201
            return self.getAllResourcesInfo()

    def deleteResource(selfself, resID):
        dao = ResourcesDAO()
        type = dao.getResourceType(resID)
        if not type:
            return jsonify(Error = "Resource not found."), 404
        else:
            dao.delete(resID, type)
            #return jsonify(DeleteStatus = "OK"), 200
            return "<h3>Resource with ID: " + resID + " was removed from the database.</h3>"

    def updateResourcePrice(self, form):
        market_price = form['market_price']
        resourceid = form['resourceID']
        if form and len(form) < 2:
            return jsonify(Error="Malformed post request"), 400
        dao = ResourcesDAO()
        if not dao.getResourceById(resourceid):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.updateResourcePrice(resourceid, market_price)
            return self.getAllResourcesInfo()

