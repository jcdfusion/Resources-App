from flask import Flask, jsonify, request
from handler.resources import ResourceHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return '<h1>Disaster Resources Site</h1>'

@app.route('/ResourcesApp/resources')
def getAllResources():
    return ResourceHandler().getAllResources()


@app.route('/ResourcesApp/resources/<int:rid>')
def getResourceById(rid):
    return ResourceHandler().getResourceById(rid)


@app.route('/ResourcesApp/resources/<string:rname>')
def getResourceByName(rname):
    return ResourceHandler().getResourceByName(rname)


@app.route('/ResourcesApp/resources/<string:rcenter>')
def getResourceByCenter(rcenter):
    return ResourceHandler().getResourceByCenter(rcenter)

if __name__ == '__main__':
    app.run()