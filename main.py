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
def getPartById(rid):
    return ResourceHandler().getResourceById(rid)


@app.route('/ResourcesApp/resources/<int:rname>')
def getPartByName(rname):
    return ResourceHandler().getResourceByName(rname)


@app.route('/ResourcesApp/resources/<int:rstore>')
def getPartByStore(rstore):
    return ResourceHandler().getResourceByStore(rstore)

if __name__ == '__main__':
    app.run()