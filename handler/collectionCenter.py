from flask import jsonify
from dao.collectionCenter import CollectionCenterDAO

class CollectionCenterHandler:

    def build_collectioncenter_dict(self, row):
        result = {}
        result['ccid'] = row[0]  # collection center id
        result['street'] = row[1]  # zipCode
        result['town'] = row[2]  # street where collection center is located
        result['state'] = row[3]  # town where collection center is located
        result['country'] = row[4]  # state where collection center is located
        result['ccname'] = row[5]  # country where collection center is located
        result['zipcode'] = row[6]  # collection center name
        return result # return result

    def build_fuel_dict(self,row):
        result={}
        result['ccid'] = row[0]
        result['rid']=row[1]
        result['fid']=row[2]
        result['fname']=row[3]
        result['brand']=row[4]
        result['octanage']=row[5]
        result['rtype']=row[6]
        result['buy_free']=row[7]
        result['market_price']=row[8]
        result['qty']=row[9]
        result['street']=row[10]
        result['town']=row[11]
        result['state_region']=row[12]
        result['country']=row[13]
        result['cname']=row[14]
        result['zipcode']=row[15]
        return result

    def build_water_dict(self,row):
        result={}
        result['ccid'] = row[0]
        result['rid']=row[1]
        result['fid']=row[2]
        result['wname']=row[3]
        result['brand']=row[4]
        result['qtyMeasure']=row[5]
        result['rtype']=row[6]
        result['buy_free']=row[7]
        result['market_price']=row[8]
        result['qty']=row[9]
        result['street']=row[10]
        result['town']=row[11]
        result['state_region']=row[12]
        result['coutry']=row[13]
        result['cname']=row[14]
        result['zipcode']=row[15]
        return result

    def build_food_dict(self,row):
        result={}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['fid'] = row[2]
        result['fname'] = row[3]
        result['brand'] = row[4]
        result['qtyweight'] = row[5]
        result['rtype'] = row[6]
        result['buy_free'] = row[7]
        result['market_price'] = row[8]
        result['qty'] = row[9]
        result['street'] = row[10]
        result['town'] = row[11]
        result['state_region'] = row[12]
        result['coutry'] = row[13]
        result['cname'] = row[14]
        result['zipcode'] = row[15]
        return result

    def build_medicalDevice_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['mdid'] = row[2]
        result['mdname'] = row[3]
        result['brand'] = row[4]
        result['manufacturer'] = row[5]
        result['treat']=row[6]
        result['rtype'] = row[7]
        result['buy_free'] = row[8]
        result['market_price'] = row[9]
        result['qty'] = row[10]
        result['street'] = row[11]
        result['town'] = row[12]
        result['state_region'] = row[13]
        result['coutry'] = row[14]
        result['cname'] = row[15]
        result['zipcode'] = row[16]
        return result

    def build_medicine_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['mid'] = row[2]
        result['mname'] = row[3]
        result['brand'] = row[4]
        result['mform'] = row[6]
        result['mmanufacturer'] = row[7]
        result['qtyweight'] = row[8]
        result['rtype'] = row[9]
        result['buy_free'] = row[10]
        result['market_price'] = row[11]
        result['qty'] = row[12]
        result['street'] = row[13]
        result['town'] = row[14]
        result['state_region'] = row[15]
        result['coutry'] = row[16]
        result['cname'] = row[17]
        result['zipcode'] = row[18]
        return result

    def build_heavyequipment_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['id'] = row[2]
        result['hetype'] = row[3]
        result['hebrand'] = row[4]
        result['rname'] = row[5]
        result['buy_free'] = row[6]
        result['market_price'] = row[7]
        result['qty'] = row[8]
        result['street'] = row[9]
        result['town'] = row[10]
        result['state_region'] = row[11]
        result['country'] = row[12]
        result['ccname'] = row[13]
        result['zipcode'] = row[14]
        return result

    def build_powergenerator_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['id'] = row[2]
        result['ptype'] = row[3]
        result['pbrand'] = row[4]
        result['pwatts']=row[5]
        result['rname'] = row[6]
        result['buy_free'] = row[7]
        result['market_price'] = row[8]
        result['qty'] = row[9]
        result['street'] = row[10]
        result['town'] = row[11]
        result['state_region'] = row[12]
        result['country'] = row[13]
        result['ccname'] = row[14]
        result['zipcode'] = row[15]
        return result

    def build_clothing_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['id'] = row[2]
        result['ctype'] = row[3]
        result['cbrand'] = row[4]
        result['ccolor'] = row[5]
        result['csize']=row[6]
        result['rname'] = row[7]
        result['buy_free'] = row[8]
        result['market_price'] = row[9]
        result['qty'] = row[10]
        result['street'] = row[11]
        result['town'] = row[12]
        result['state_region'] = row[13]
        result['country'] = row[14]
        result['ccname'] = row[15]
        result['zipcode'] = row[16]
        return result

    def build_battery_dict(self,row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['id'] = row[2]
        result['btype'] = row[3]
        result['bbrand'] = row[4]
        result['bvoltage'] = row[5]
        result['rname'] = row[6]
        result['buy_free'] = row[7]
        result['market_price'] = row[8]
        result['qty'] = row[9]
        result['street'] = row[10]
        result['town'] = row[11]
        result['state_region'] = row[12]
        result['country'] = row[13]
        result['ccname'] = row[14]
        result['zipcode'] = row[15]
        return result

    def build_tools_dict(self,row):
        result={}
        result['ccid']=row[0]
        result['rid']=row[1]
        result['id']=row[2]
        result['ttype']=row[3]
        result['tbrand']=row[4]
        result['rname']=row[5]
        result['buy_free']=row[6]
        result['market_price']=row[7]
        result['qty']=row[8]
        result['street']=row[9]
        result['town']=row[10]
        result['state_region']=row[11]
        result['country']=row[12]
        result['ccname']=row[13]
        result['zipcode']=row[14]
        return result

    def build_ice_dict(self,row):
        result={}
        result['ccid']=row[0]
        result['rid']=row[1]
        result['id']=row[2]
        result['ibrand']=row[3]
        result['rname']=row[4]
        result['buy_free']=row[5]
        result['market_price']=row[6]
        result['qty']=row[7]
        result['street']=row[8]
        result['town']=row[9]
        result['state_region']=row[10]
        result['country']=row[11]
        result['ccname']=row[12]
        result['zipcode']=row[13]
        return result





    def build_resources_dict(self, row):
        result = {}
        result['resourceid'] = row[0]  # resource id
        result['ccid'] = row[1]  # collection center id
        result['rname'] = row[2]  # resource name
        result['buy_free'] = row[3]  # boolean whether the resource is free or not
        result['rprice'] = row[4]  # resource price
        result['qty'] = row[5]  # resource qty
        return result

    def build_resourcetype_dict(self, row):
        result = {}
        result['rtid'] = row[0] #resource type id
        result['rname'] = row[1] #resource type name
        return result

    def build_ccByresourceType_dict(self,row):
        result={}
        result['ccid']=row[0]
        result['rid']=row[1]
        result['id']=row[2]
        result['rtype']=row[3]
        result['rbrand']=row[4]
        result['rname']=row[5]
        result['buy_free']=row[6]
        result['market_price']=row[7]
        result['qty']=row[8]
        result['street']=row[9]
        result['town']=row[10]
        result['state_region']=row[11]
        result['country']=row[12]
        result['ccname']=row[13]
        result['zipcode']=row[14]
        return result

    def build_resourcepurchasedByCC_dict(self, row):
        result = {}
        result['ccid'] = row[0]
        result['rid'] = row[1]
        result['id'] = row[2]
        result['rtype'] = row[3]
        result['rbrand'] = row[4]
        result['rname'] = row[5]
        result['buy_free'] = row[6]
        result['market_price'] = row[7]
        result['qty'] = row[8]
        result['pid'] = row[9]
        result['userid'] = row[10]
        result['rqstid'] = row[11]
        result['ccnum'] = row[12]
        result['rqty'] = row[13]
        result['street'] = row[14]
        result['town'] = row[15]
        result['state_region'] = row[16]
        result['country'] = row[17]
        result['ccname'] = row[18]
        result['zipcode'] = row[19]
        return result
    
    def build_announcement_dict(self,row):
        result={}
        result['rtype'] = row[0]
        result['qty']=row[1]
        result['ccname']=row[2]
        result['town']=row[3]
        result['state']=row[4]
        result['country']=row[5]
        return result



    def getAllCenters(self):
        dao = CollectionCenterDAO()
        location_list = dao.getAllCenters()
        result_list = []
        for row in location_list:
            result = self.build_collectioncenter_dict(row)
            result_list.append(result)
        return jsonify(CollectionCenter=result_list)

    def searchCenter(self,args):
        ccid = args.get('ccid')
        ccname = args.get('ccname')
        street = args.get('street')
        town = args.get('town')
        state = args.get('state')
        country = args.get('country')
        zipcode = args.get('zipcode')
        rtid = args.get('rtid')
        rtype =args.get('rtype')
        rname = args.get('rname')
        ravailable= args.get('ravailable')
        ccorders = args.get('ccorders')
        watts = args.get('watts')
        bvoltage =args.get('bvoltage')


        dao = CollectionCenterDAO()
        if(len(args)==1) and ccid:
            collectioncenter_list = dao.getCenterByID(ccid)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_collectioncenter_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

        if (len(args) == 1) and ccname:
            collectioncenter_list = dao.getResourcesAvailable(ccname)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

        elif (len(args) == 1) and street:
            collectioncenter_list = dao.getCenterByStreet(street)

        elif (len(args) == 1) and town:
            collectioncenter_list = dao.getCenterByTown(town)

        elif (len(args) == 1) and country:
            collectioncenter_list = dao.getCenterByCountry(country)

        elif (len(args) == 1) and zipcode:
            collectioncenter_list = dao.getCenterByZip(zipcode)

        elif (len(args)==2) and ccorders and ccname:
            collectioncenter_list = dao.getOrdersbyCCName(ccname)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_resourcepurchasedByCC_dict(row)
                result_list.append(result)
            return jsonify(OrdersByCollectionCenter=result_list)

        #FUEL
        elif(len(args)==1) and rname=='fuel':
            collectioncenter_list = dao.getCenterByFuel(rname)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel=result_list)

        elif (len(args) == 2) and rname=='fuel' and (rtype) : #fueltype
            collectioncenter_list = dao.getCenterByFuelType(rtype)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel=result_list)

        elif (len(args) == 3) and rname=='fuel' and (rtype) and (country or state or town):
            if (country):
                collectioncenter_list = dao.getCenterByFuelTypeAndCountry(rtype,country)
            elif (state):
                collectioncenter_list = dao.getCenterByFuelTypeAndState(rtype, state)
            elif(town):
                collectioncenter_list = dao.getCenterByFuelTypeAndTown(rtype, town)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel=result_list)
        ##=======================================================================================================##

            # Water
        elif (len(args) ==1) and rname=='water':
            collectioncenter_list = dao.getCenterByWater()

            result_list = []
            for row in collectioncenter_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water=result_list)

        elif(len(args)==2) and rname=='water' and (state or country or town):
            if(state):
                collectioncenter_list = dao.getCenterByWaterAndState(state)
            elif(country):
                collectioncenter_list = dao.getCenterByWaterAndCountry(country)
            elif(town):
                collectioncenter_list = dao.getCenterByWaterAndTown(town)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water=result_list)

        elif (len(args) == 2) and rname == 'water' and rtype:  # watertype
            collectioncenter_list = dao.getCenterByWaterType(rtype)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water=result_list)

        elif (len(args) == 3) and rname=='water' and (rtype) and (country or state or town):
            if (country):
                collectioncenter_list = dao.getCenterByWaterTypeAndCountry(rtype, country)
            elif (state):
                collectioncenter_list = dao.getCenterByWaterTypeAndState(rtype, state)
            elif (town):
                collectioncenter_list = dao.getCenterByWaterTypeAndTown(rtype, town)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water=result_list)
    ##===============================================================================================================##


    ##FOOD

        elif (len(args) == 1) and rname == 'food':
            collectioncenter_list = dao.getCenterByFood()

            result_list = []
            for row in collectioncenter_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(FOOD=result_list)

        elif (len(args) == 2) and rname == 'food' and (state or country or town):
            if (state):
                collectioncenter_list = dao.getCenterByFoodAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByFoodAndCountry(country)
            elif (town):
                collectioncenter_list = dao.getCenterByFoodAndTown(town)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(Food=result_list)


        elif (len(args) == 2) and rname=='food' and rtype:
            collectioncenter_list = dao.getCenterByFoodType(rtype)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(FOOD=result_list)


        elif (len(args) == 3) and rname == 'food' and rtype and (state or country or town):
            if (state):
                collectioncenter_list = dao.getCenterByFoodTypeAndState(rtype,state)
            elif (country):
                collectioncenter_list = dao.getCenterByFoodTypeAndCountry(rtype,country)
            elif (town):
                collectioncenter_list = dao.getCenterByFoodTypeAndTown(rtype,town)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(Food=result_list)
#####################################################################################

        elif (len(args) == 3) and rname=='food'and rtype and (country or state or town):
            if (country):
                collectioncenter_list = dao.getCenterByFoodTypeAndCountry(rtype, country)
            elif (state):
                collectioncenter_list = dao.getCenterByFoodTypeAndState(rtype, state)
            elif (town):
                collectioncenter_list = dao.getCenterByFoodTypeAndTown(rtype, town)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(FOOD=result_list)
    ##================================================================================================================##

    ##MEDICINE
        elif(len(args)==1) and rname =='medicine':
            collectioncenter_list= dao.getCenterByMedicine()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_medicine_dict(row)
                result_list.append(result)
            return jsonify(Medicine=result_list)

        elif (len(args) == 2) and (rname == 'medicine') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByMedicineAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByMedicineAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByMedicineAndCountry(country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_medicine_dict(row)
                result_list.append(result)
            return jsonify(Medicine=result_list)
    ##================================================================================================================##

    ##HEAVY EQUIPMENT

        elif (len(args) == 1) and rname == 'heavyequipment':
            collectioncenter_list = dao.getCenterByHeavyEquipment()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_heavyequipment_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquipment=result_list)

        elif (len(args) == 2) and (rname == 'heavyequipment') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByHeavyEquipmentAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByHeavyEquipmentAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByHeavyEquipmentAndCountry(country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_heavyequipment_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquipment=result_list)



    ##================================================================================================================##

            ##POWER GENERATORS

        elif (len(args) == 1) and rname == 'powergenerator':
            collectioncenter_list = dao.getCenterByPowerGenerator()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_powergenerator_dict(row)
                result_list.append(result)
            return jsonify(POWERGENERATOR=result_list)

        elif (len(args) == 2) and (rname == 'powergenerator') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndCountry(country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_powergenerator_dict(row)
                result_list.append(result)
            return jsonify(POWERGENERATOR=result_list)

        elif (len(args)==2) and (rname == 'powergenerator') and watts:

            collectioncenter_list = dao.getCenterByPowerGeneratorAndWatts(watts)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_powergenerator_dict(row)
                result_list.append(result)
            return jsonify(POWERGENERATOR=result_list)

        elif (len(args) == 3) and (rname == 'powergenerator') and watts and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndWattsAndTown(watts,town)
            elif (state):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndWattsAndState(watts,state)
            elif (country):
                collectioncenter_list = dao.getCenterByPowerGeneratorAndWattsAndCountry(watts,country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_powergenerator_dict(row)
                result_list.append(result)
            return jsonify(POWERGENERATOR=result_list)



            ##================================================================================================================##
            ##================================================================================================================##

            ##CLOTHING

        elif (len(args) == 1) and rname == 'clothing':
            collectioncenter_list = dao.getCenterByClothing()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_clothing_dict(row)
                result_list.append(result)
            return jsonify(CLOTHING=result_list)

        elif (len(args) == 2) and (rname == 'clothing') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByClothingAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByClothingAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByClothingAndCountry(country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_clothing_dict(row)
                result_list.append(result)
            return jsonify(CLOTHING=result_list)




    ##================================================================================================================##

            ##BATTERY

        elif (len(args) == 1) and rname == 'battery':
            collectioncenter_list = dao.getCenterByBattery()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(BATTERY=result_list)

        elif (len(args) == 2) and (rname == 'battery') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByBatteryAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByBatteryAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByBatteryAndCountry(country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(BATERRY=result_list)

        elif (len(args)==2) and (rname=='battery') and bvoltage:
            collectioncenter_list = dao.getCenterByBatteryAndBVoltage(bvoltage)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(BATERRY=result_list)

        elif (len(args)==3) and (rname=='battery') and bvoltage and (country or state or town):

            if (town):
                collectioncenter_list = dao.getCenterByBatteryAndBVoltageAndTown(bvoltage,town)
            elif (state):
                collectioncenter_list = dao.getCenterByBatteryAndBVoltageAndState(bvoltage,state)
            elif (country):
                collectioncenter_list = dao.getCenterByBatteryAndBVoltageAndCountry(bvoltage,country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(BATERRY=result_list)




        ##============================================================================================================##

        ##TOOLS
        elif (len(args) == 1) and rname == 'tools':
            collectioncenter_list = dao.getCenterByTools()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
            return jsonify(TOOLS=result_list)

        elif (len(args) == 2) and (rname == 'tools') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByToolsAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByToolsAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByToolsAndCountry(country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
            return jsonify(TOOLS=result_list)
        ##============================================================================================================##

        #ICE

        elif (len(args) == 1) and rname == 'ice':
            collectioncenter_list = dao.getCenterByIce()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(ICE=result_list)

        elif (len(args) == 2) and (rname == 'ice') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByIceAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByIceAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByIceAndCountry(country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(ICE=result_list)

        ##============================================================================================================##



    ##MEDICAL DEVICES
        elif(len(args)==1) and rname=='md':
            collectioncenter_list = dao.getCenterByMedicalDevices()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_medicalDevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevices=result_list)

        elif (len(args) == 2) and (rname=='md') and (country or state or town):
            if (town):
                collectioncenter_list = dao.getCenterByMedicalDeviceAndTown(town)
            elif (state):
                collectioncenter_list = dao.getCenterByMedicalDeviceAndState(state)
            elif (country):
                collectioncenter_list = dao.getCenterByMedicalDeviceAndCountry(country)

            result_list = []
            for row in collectioncenter_list:
                result = self.build_medicalDevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevices=result_list)
    ##================================================================================================================##

        elif (len(args)==1) and ravailable:
            collectioncenter_list= dao.getCenterByResourcesAvailable()
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(ResourcesAvailable=result_list)

        elif (len(args)==2) and ravailable and ccname:
            collectioncenter_list= dao.getCenterByResourcesAvailableAndCenterName(ccname)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(ResourcesAvailable=result_list)

        elif (len(args)==2) and ravailable and country:
            collectioncenter_list= dao.getCenterByResourcesAvailableAndCountry(country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(ResourcesAvailable=result_list)

        elif (len(args)==2) and ravailable and state:
            collectioncenter_list= dao.getCenterByResourcesAvailableAndState(state)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(ResourcesAvailable=result_list)

        elif (len(args)==2) and ravailable and town:
            collectioncenter_list= dao.getCenterByResourcesAvailableAndTown(town)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(ResourcesAvailable=result_list)


        elif (len(args)==1) and rtype: #specific resource type of resource
            collectioncenter_list = dao.getCenterByResourceType(rtype)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(CollectionCenter=result_list)

        elif (len(args)==2) and rtype and country:
            collectioncenter_list = dao.getCenterByResourceTypeAndCountry(rtype,country)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(CollectionCenter=result_list)

        elif (len(args) == 2) and rtype and state:
            collectioncenter_list = dao.getCenterByResourceTypeAndState(rtype, state)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(CollectionCenter=result_list)

        elif (len(args) == 2) and rtype and town:
            collectioncenter_list = dao.getCenterByResourceTypeAndTown(rtype, town)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(CollectionCenter=result_list)

        elif (len(args) == 2) and rtype and ccname:
            collectioncenter_list = dao.getCenterByResourceTypeAndCenterName(rtype, ccname)
            result_list = []
            for row in collectioncenter_list:
                result = self.build_ccByresourceType_dict(row)
                result_list.append(result)
            return jsonify(CollectionCenter=result_list)
        
       # elif(len(args)==1) and announcement:
        #    collectioncenter_list = dao.getAnnouncementResources()
         #   result_list=[]
          #  for row in collectioncenter_list:
           #     result = self.build_announcement_dict(row)
            #    result_list.append(result)
            #return jsonify(Annoucemnet=result_list)

        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in collectioncenter_list:
            result = self.build_collectioncenter_dict(row)
            result_list.append(result)
        return jsonify(CollectionCenter=result_list)

    def getAllResources(self):
        dao = CollectionCenterDAO()
        collectioncenter_list = dao.getCenterByResourcesAvailable()
        result_list = []
        for row in collectioncenter_list:
            result = self.build_ccByresourceType_dict(row)
            result_list.append(result)
        return jsonify(CollectionCenter=result_list)


    def getCenterByZip(self, zipCode):
        dao = CollectionCenterDAO()
        row = dao.getCenterByZip(zipCode)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location = location)

    def getCenterByStreet(self, street):
        dao = CollectionCenterDAO()
        row = dao.getCenterByStreet(street)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location=location)

    def getCenterByTown(self, town):
        dao = CollectionCenterDAO()
        row = dao.getCenterByTown(town)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location=location)

    def getCenterByState(self, state):
        dao = CollectionCenterDAO()
        row = dao.getCenterByState(state)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location=location)

    def getCenterByCountry(self, country):
        dao = CollectionCenterDAO()
        row = dao.getCenterByCountry(country)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location = location)

    def getCenterByName(self, ccname):
        dao = CollectionCenterDAO()
        row = dao.getCenterByName(ccname)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location = location)

    def insertCollectionCenter(self, form):
        if form and len(form) == 6:
            ccname = form['ccname']
            street = form['street']
            town = form['town']
            state = form['state']
            country = form['country']
            zipcode = form['zipcode']
            if ccname and street and town and state and country and zipcode:
                dao = CollectionCenterDAO()
                ccid = dao.insert(ccname, street, town, state, country, zipcode)
                result = {}
                result['ccid'] = ccid
                result['street'] = street
                result['town'] = town
                result['state'] = state
                result['country'] = country
                result['ccname'] = ccname
                result['zipcode'] = zipcode
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def deleteCollectionCenter(selfself, ccid):
        dao = CollectionCenterDAO()
        if not dao.getCenterByID(ccid):
            return jsonify(Error = "Center not found."), 404
        else:
            dao.delete(ccid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateCollectionCenter(self, ccid, form):
        dao = CollectionCenterDAO()
        if not dao.getCenterByID(ccid):
            return jsonify(Error="Center not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                ccname = form['ccname']
                street = form['street']
                town = form['town']
                state = form['state']
                country = form['country']
                zipcode = form['zipcode']
                if ccname and street and town and state and country and zipcode:
                    dao.update(ccid, ccname, street, town, state, country, zipcode)
                    result = self.build_collectioncenter_attributes(ccid, ccname, street, town, state, country, zipcode)
                    return jsonify(Center=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


