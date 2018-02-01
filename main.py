from flask import Flask, jsonify, request
from handler.resources import ResourceHandler
from handler.users import UsersHandler
from handler.collectionCenter import CollectionCenterHandler
import psycopg2

app = Flask(__name__)

@app.route('/')
def greeting():
    return '<h1>Disaster Resources Site</h1>'

@app.route('/ResourceApp/resources', methods=['GET','POST','DELETE'])
def getResources():
    formData = request.form
    print(formData)
    if request.method == 'POST':
        print(formData)
        print(len(formData))
        return ResourceHandler().insertResource(formData)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(formData)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)

@app.route('/ResourceApp/resources/<int:resourceID>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(resourceID):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(resourceID)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(resourceID, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(resourceID)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/<string:rtype>',methods=['GET', 'PUT', 'DELETE'])
def getResourceByName(rtype):
    if request.method == 'GET':
        return ResourceHandler().getResourceByName(rtype)
    elif request.method == 'PUT':
        return ResourceHandler().updateResourceName(rtype, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResourceName(rtype)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/<string:rcenter>',methods=['GET','PUT','DELETE'])
def getResourceByCenter(rcenter):

        if request.method == 'GET':
            return ResourceHandler.getResourceByCenter(rcenter)
        elif request.method == 'PUT':
            return ResourceHandler().updateResourceCenter(rcenter, request.form)
        elif request.method == 'DELETE':
            return ResourceHandler().deleteResourceCenter(rcenter)
        else:
            return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/<int:rid>/center')
def getCenterbyResourceID(rid):
    return ResourceHandler.getCenterByResourceID(rid)

#==========Collection Center Routing==============#
@app.route('/ResourceApp/center', methods=['GET', 'POST', 'PUT'])
def getAllCollectionCenter():
    if request.method == 'POST':
        return CollectionCenterHandler().insertCollectionCenter(request.form)
    elif request.method == 'PUT':
        return CollectionCenterHandler().updateCollectionCenter(request.form)
    else:
        if not request.args:
            return CollectionCenterHandler().getAllCenters()
        else:
            return CollectionCenterHandler().searchCenter(request.args)

#======= User Routing ========#

@app.route('/ResourceApp/users', methods=['GET', 'POST', 'PUT'])
def getUsers():
    if request.method == 'POST':
        return UsersHandler().insertUser(request.form)
    elif request.method == 'PUT':
        return UsersHandler().updateUser(request.form)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().searchUsers(request.args)

@app.route('/ResourceApp/login')
def login():
        return UsersHandler().userLogin(request.args)


@app.route('/ResourceApp/users/requests')
def getUserRequest():
    if not request.args:
        return UsersHandler().getAllRequests()
    return UsersHandler().searchUsersRequests(request.args)


if __name__ == '__main__':
    app.run()
