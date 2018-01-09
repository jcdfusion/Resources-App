from flask import jsonify
from dao.collectionCenter import CollectionCenterDAO

class CollectionCenterHandler:

    def build_collectionCenter_dict(self, row):
        result = {}
        result['ccid'] = row[0]  # collection center id
        result['zipCode'] = row[1]  # zipCode
        result['street'] = row[2]  # street where collection center is located
        result['town'] = row[3]  # town where collection center is located
        result['state'] = row[4]  # state where collection center is located
        result['country'] = row[5]  # country where collection center is located
        result['ccname'] = row[6]  # collection center name
        return result # return result

    def getAllCenters(self):
        dao = CollectionCenterDAO()
        location_list = dao.getAllCenters()
        result_list = []
        for row in location_list:
            result = self.build_collectionCenter_dict(row)
            result_list.append(result)
        return jsonify(Location=result_list)

    def getCenterByZip(self, zip):
        dao = CollectionCenterDAO()
        row = dao.getCenterByZip(zip)
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

    def getCenterByName(self, name):
        dao = CollectionCenterDAO()
        row = dao.getCenterByName(name)
        if not row:
            return jsonify(Error="Collection Center Not Found"), 404
        else:
            location = self.build_collectionCenter_dict(row)
            return jsonify(Location = location)