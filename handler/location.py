from flask import jsonify
from dao.location import LocationDAO

class LocationHandler:

    def build_location_dict(self, row):
        result = {}
        result['zip'] = row[0]  # location zip-code
        result['cid'] = row[1]  # location country Id
        result['sid'] = row[2]  # location State/Region Id
        result['tid'] = row[3]  # location town Id
        return result

    def locationError(self):
        return jsonify(Error = "Location Not Found"), 404

    def getAllLocations(self):
        dao = LocationDAO()
        location_list = dao.getAllLocations()
        result_list = []
        for row in location_list:
            result = self.build_location_dict(row)
            result_list.append(result)
        return jsonify(Location=result_list)

    def getLocationByZip(self, zip):
        dao = LocationDAO()
        row = dao.getLocationByZip(zip)
        if not row:
            locationError()
        else:
            location = self.build_location_dict(row)
            return jsonify(Location = location)

    def getLocationByCountryID(self, cid):
        dao = LocationDAO()
        row = dao.getLocationByCountryID(cid)
        if not row:
            locationError()
        else:
            location = self.build_location_dict(row)
            return jsonify(Location = location)

    def getLocationByStateID(self, sid):
        dao = LocationDAO()
        row = dao.getLocationByStateID(sid)
        if not row:
            locationError()
        else:
            location = self.build_location_dict(row)
            return jsonify(Location=location)

    def getLocationByTownID(self, tid):
        dao = LocationDAO()
        row = dao.getLocationByTownID(tid)
        if not row:
            locationError()
        else:
            location = self.build_location_dict(row)
            return jsonify(Location=location)