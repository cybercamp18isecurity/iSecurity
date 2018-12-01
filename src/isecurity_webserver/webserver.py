import flask
import os
import time
myPath = os.path.dirname(os.path.abspath(__file__))

from flask import jsonify

from .devices import Devices
from .users import Users

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def menu():
    pass

@app.route('/devices', methods = ['GET'])
def getDevices():
    devices = Devices()
    devices_data = devices.get_list_devices()
    return jsonify(devices_data)

@app.route('/users', methods = ['GET'])
def getUsers():
    return jsonify(Users.get_list_users())

@app.route('/alerts', methods = ['GET'])
def getAlerts():
    return jsonify([{
        "date": time.time(),
        "id_external": "fasf234asdfasdf",
        "id_user": "fasdf23asdf",
        "type": "Manipulación de red",
        "status": 1,
        "criticity": 6,
        "description": "Manipulación de paquetes desde la red interna....",
        "is_deleted": False,
        "events": []
    }])

@app.route('/domains', methods = ['GET'])
def getDomains():
    return jsonify([{
        "timestamp": time.time(),
        "url": "https://pigram.luca-d3.com",
        "ip": "14.172.234.12",
        "domain": "",
        "description": "Pigram es un servicio que permite....",
        "owner": "Javi pelos",
        "img_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/Avatar%20Background.png?alt=media&token=316d1cf5-2f34-4ec5-87d8-304e686bdf36",
        "old_img_url": "",
        "status": 1,
        "isDeleted": False,
        "htmlcode_url": "",
        "old_htmlcode_url": "",
        "events": []
    }])


@app.route('/summary', methods = ['GET'])
def getSummary():
    return jsonify()

from .devices.devices import device_pages

app.register_blueprint(device_pages)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True)
