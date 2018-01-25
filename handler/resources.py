from flask import jsonify
from dao.resources import ResourcesDAO
from dao.collectionCenter import CollectionCenterDAO


class ResourceHandler:

    def build_resources_dict(self,row):
        result={}
        result['resourceid']=row[0] #resource id
        result['ccid'] = row[1] #collection center id
        result['rname'] = row[2] #resource name id
        result['buy_free'] = row[3] #boolean whether the resource is free or not
        result['rprice'] = row[4] #resource price
        result['qty'] = row[5] #resource qty
        return result

    def build_resourcetype_dict(self, row):
        result = {}
        result['rtid'] = row[0] #resource type id
        result['rname'] = row[1] #resource name
        return result


    def build_collectionCenter_dict(self,row):
        result={}
        result['ccid']=row[0] #collection center id
        result['zipCode']=row[1] #zipCode
        result['street']=row[2] #street where collection center is located
        result['ccname']=row[3] #collection center name
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
        result['buy_free']=row[7]
        return result


    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResources(self, args):
        rid = args.get('rid')
        rname = args.get('rname')
        rtype = args.get('rtype')
        buy_free = args.get('buy_free')
        dao = ResourcesDAO()

        if (len(args) == 1) and rid:
            resources_list = dao.getResourceById(rid)

        elif(len(args)==1) and rname:
            resources_list = dao.getResourceInfoByName(rname)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInfo_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif(len(args)==1) and rtype:
            resources_list = dao.getResourceInfoByType(rtype)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInfo_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        elif(len(args)==1) and buy_free:
            resources_list = dao.getResourceInfoByBF(buy_free)
            result_list = []
            for row in resources_list:
                result = self.build_resourcesInfo_dict(row)
                result_list.append(result)
            return jsonify(Resource=result_list)

        else:
            return jsonify(Error="Malformed query string"), 400
        result_list=[]
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def insertResource(self, form):
        if len(form) < 5:
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
                qtyMeasure = form['qtyMeasure']
                if waterType and waterBrand and qtyMeasure:
                    rid = dao.insertWater(resID, waterType, resID, waterBrand, qtyMeasure)
            elif resourceType == 'food':
                foodTypeID = form['foodTypeID']
                foodName = form['foodName']
                qtyWeight = form['qtyWeight']
                if foodTypeID and foodName and qtyWeight:
                    rid = dao.insertFood(resID, foodTypeID, foodName, qtyWeight)
            elif resourceType == 'ice':
                iceBrand = form['iceBrand']
                qtyWeight = form['qtyWeight']
                if iceBrand and qtyWeight:
                    rid = dao.insertIce(resID, iceBrand, qtyWeight)
            elif resourceType == 'clothing':
                clothingType = form['clothingType']
                clothing_size = form['clothing_size']
                if clothingType and clothing_size:
                    rid = dao.insertClothing(resID, clothingType, clothing_size)
            elif resourceType == 'gas':
                gasTypeID = form['gasTypeID']
                gasBrand = form['gasBrand']
                gasOctanage = form['gasOctanage']
                qty = form['qty']
                if gasTypeID and gasBrand and gasOctanage and qty:
                    rid = dao.insertGas(resID, gasTypeID, gasBrand, gasOctanage, qty)
            elif resourceType == 'medicalDevices':
                medicalDeviceType = form['medicalDeviceType']
                medDevName = form['medDevName']
                medDevManufacturer = form['medDevManufacturer']
                toTreat = form['toTreat']
                qty = form['qty']
                if medicalDeviceType and medDevName and medDevManufacturer and toTreat and qty:
                    rid = dao.insertMedical(resID, medicalDeviceType, medDevName, medDevManufacturer, toTreat, qty)
            elif resourceType == 'heavyEquipment':
                heavyEquipmentType = form['heavyEquipmentType']
                heavyEquipmentBrand = form['heavyEquipmentBrand']
                if heavyEquipmentType and heavyEquipmentBrand:
                    rid = dao.insertHeavy(resID, heavyEquipmentType, heavyEquipmentBrand)
            elif resourceType == 'tools':
                toolType = form['toolType']
                toolBrand = form['toolBrand']
                qty = form['qty']
                if toolType and toolBrand and qty:
                    rid = dao.insertTools(resID, toolType, toolBrand, qty)
            elif resourceType == 'powerGenerator':
                powerGeneratorType = form['powerGeneratorType']
                powerGeneratorBrand = form['powerGeneratorBrand']
                watts = form['watts']
                qty = form['qty']
                if powerGeneratorType and powerGeneratorBrand and watts and qty:
                    rid = dao.insertPower(resID, powerGeneratorType, powerGeneratorBrand, watts, qty)
            elif resourceType == 'batteries':
                batteryType = form['batteryType']
                batteryBrand = form['batteryBrand']
                batteryVoltage = form['batteryVoltage']
                qty = form['qty']
                if batteryType and batteryBrand and batteryVoltage and qty:
                    rid = dao.insertBatteries(resID, batteryType, batteryBrand, batteryVoltage, qty)
            elif resourceType == 'medicicne':
                medicineType = form['medicineType']
                medicine_form = form['medicine_form']
                medicine_name = form['medicine_name']
                medicine_exp_date = form['medicine_exp_date']
                medicine_manufacturer = form['medicine_manufacturer']
                v = form['v']
                if medicineType and medicine_form and medicine_name and medicine_exp_date and medicine_manufacturer and v:
                    rid = dao.insertMedicine(resID, medicineType, medicine_form, medicine_name, medicine_exp_date, medicine_manufacturer, v)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
            result = self.build_resourcesInfo_dict(resID, collectionCenterID, resourceType, buy_free, market_price, resQty)
            return jsonify(Resource=result), 201

    def deleteResource(selfself, resID):
        dao = ResourcesDAO()
        type = dao.getResourceType(resID)
        if not type:
            return jsonify(Error = "Resource not found."), 404
        else:
            dao.delete(resID, type)
            return jsonify(DeleteStatus = "OK"), 200