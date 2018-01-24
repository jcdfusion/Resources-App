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

    def build_collectioncenter_attributes(self, ccid, ccname, street, town, state, country, zipcode):
        result = {}
        result['ccname'] = ccname
        result['street'] = street
        result['town'] = town
        result['state'] = state
        result['country'] = country
        result['zipcode'] = zipcode
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



    def getAllCenters(self):
        dao = CollectionCenterDAO()
        location_list = dao.getAllCenters()
        result_list = []
        for row in location_list:
            result = self.build_collectioncenter_dict(row)
            result_list.append(result)
        return jsonify(CollectionCenter=result_list)

    def searchCenter(self,args):
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

        dao = CollectionCenterDAO()
        if (len(args) == 1) and ccname:
            collectioncenter_list = dao.getCenterByName(ccname)

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

        elif (len(args) == 1) and rname : #resource name
            collectioncenter_list = dao.getCenterByResourceName(rname)

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

        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in collectioncenter_list:
            result = self.build_collectioncenter_dict(row)
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