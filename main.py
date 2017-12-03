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
def getPartById():
    return ResourceHandler().getRecourceById()


@app.route('/ResourcesApp/resources/<int:rname>')
def getPartByName():
    return ResourceHandler().getRecourceByName()


@app.route('/ResourcesApp/resources/<int:rstore>')
def getPartByStore():
    return ResourceHandler().getRecourceByStore()

if __name__ == '__main__':
    app.run()