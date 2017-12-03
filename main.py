from flask import Flask, jsonify, request
from handler.resources import ResourceHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Disaster Resources Site'

@app.route('/ResourcesApp/resources')
def getAllResources():
    return ResourceHandler().getAllResources()


@app.route('/ResourcesApp/resources/<int:rid>')
def getPartById(rid):
    return ResourceHandler().getRecourceById(rid)


@app.route('/ResourcesApp/resources/<int:rname>')
def getPartByName(rname):
    return ResourceHandler().getRecourceByName(rname)


@app.route('/ResourcesApp/resources/<int:rstore>')
def getPartByStore(rstore):
    return ResourceHandler().getRecourceByStore(rstore)

if __name__ == '__main__':
    app.run()