from flask import jsonify
from dao.collectionCenter import CollectionCenterDAO

class CollectionCenterHandler:

    def build_collectionCenter_dict(self, row):
        result = {}
        result['ccid'] = row[0]  # collection center id
        result['zipCode'] = row[1]  # zipCode
        result['street'] = row[2]  # street where collection center is located
        result['ccname'] = row[3]  # collection center name
        return result # return result