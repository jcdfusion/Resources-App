from flask import jsonify
from dao.resources import ResourcesDAO


class ResourceHandler:
    def build_resourcetype_dict(self, row):
        result = {}
        result['rtid'] = row[0] #resource type id
        result['rname'] = row[1] #resource type name
        return result

    def build_resources_dict(self,row):
        result={}
        result['rid']=row[0] #resource id
        result['ccid'] = row[1] #collection center id
        result['rtid'] = row[2] #resource type id
        result['buy_free'] = row[3] #boolean whether the resource is free or not
        result['rprice'] = row[4] #resource price
        result['qty'] = row[5] #resource qty
        return result

    def build_collectionCenter_dict(self,row):
        result={}
        result['ccid']=row[0] #collection center id
        result['zipCode']=row[1] #zipCode
        result['street']=row[2] #street where collection center is located
        result['ccname']=row[3] #collection center name
        return result


    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resourcetype_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resources = resource)

    def getResourceByName(self, rname):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resourcetype_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getResourceByCenter(self, rcenter):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resourcetype_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceByLocation(self,location):
        dao=ResourcesDAO()
        row = dao.getResourceByLocation(location)
        if not row:
            return jsonify(Error="Not Found"), 404
        else:
            resource = self.build_resourcetype_dict(row)
        return jsonify(Resource=resource)