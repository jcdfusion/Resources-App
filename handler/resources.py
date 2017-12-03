from flask import jsonify
from dao.resources import ResourcesDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, rid):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceByName(self, rname):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getResourceByStore(self, rstore):
        dao = ResourcesDAO()
        resources_list = dao.getAllResorces()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)