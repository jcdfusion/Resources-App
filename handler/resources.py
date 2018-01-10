from flask import jsonify
from dao.resources import ResourcesDAO


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
