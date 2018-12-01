import os
import time
myPath = os.path.dirname(os.path.abspath(__file__))

import flask
from flask import jsonify, request

from isecurity_webserver.devices import Devices
from isecurity_webserver.users import Users
from isecurity_webserver.alerts import Alerts

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def menu():
    return None

### DEVICES ###
@app.route('/devices', methods = ['GET'])
def get_devices():
    max_count = request.args.get('number')

    devices = Devices()
    devices_data = devices.get_list_devices(max_count)
    return jsonify(devices_data)

@app.route('/devices/<id_device>', methods = ['GET'])
def get_info_device(id_device):

    devices = Devices()
    device_data = devices.get_details_device(id_device)
    return jsonify(device_data)

### USERS ###
@app.route('/users', methods = ['GET'])
def get_users():
    max_count = request.args.get('number')

    users_endpoint = Users()
    users_data = users_endpoint.get_list_users(max_count)
    return jsonify(users_data)

@app.route('/users/<id_user>', methods = ['GET'])
def get_info_user(id_user):
    user_endpoint = Users()
    user_data = user_endpoint.get_user_details(id_user)
    return jsonify(user_data)

@app.route('/users/<id_user>/update', methods = ['POST'])
def update_status_user(id_user):
    status = request.args.get('status')
    user_endpoint = Users()
    ok = user_endpoint.update_user_status(id_user, status)
    return jsonify({"status": ok})


### Alertas
@app.route('/alerts', methods = ['GET'])
def get_alerts():
    max_count = request.args.get('number')
    alert_endpoint = Alerts()
    alerts_data = alert_endpoint.get_list_alerts(max_count)
    return jsonify(alerts_data)

@app.route('/alerts/<id_alert>', methods = ['GET'])
def get_info_alert(id_alert):
    alert_endpoint = Alerts()
    alert_data = alert_endpoint.get_alert_details(id_alert)
    return jsonify(alert_data)

@app.route('/alerts/<id_alert>/update', methods = ['POST', 'GET'])
def update_status_alert(id_alert):
    status = request.args.get('status')

    alert_endpoint = Alerts()
    ok = alert_endpoint.update_alert_status(id_alert, status)
    return jsonify({"status": ok})


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


if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True)
