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
