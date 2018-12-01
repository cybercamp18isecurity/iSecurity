import flask
import os
import time
myPath = os.path.dirname(os.path.abspath(__file__))

from flask import jsonify

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def menu():
    pass

@app.route('/devices', methods = ['GET'])
def getDevices():
    return jsonify(
        [{
                "timestamp": time.time(),
                "hostname": "Dell XPS 15",
                "owner": "Santiago Hernandez",
                "avatar_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/hpspectre.jpg?alt=media&token=2d09092c-7c2d-43ec-bd79-0596b1596b9f",
                "status": 1
            },
            {
                "timestamp": time.time(),
                "hostname": "HP Pavilion",
                "owner": "Becario",
                "avatar_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/hppavilion.png?alt=media&token=4c3940cb-d5d5-47d4-a863-c3c366f3b36a",
                "status": 0
            },
            {
                "timestamp": time.time(),
                "hostname": "Macbook Pro 15",
                "owner": "Lucas Fernández",
                "avatar_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/macbookpro.jpg?alt=media&token=6c04c132-933a-449c-94a9-945eec97fe04",
                "status": 0
            },
            {
                "timestamp": time.time(),
                "hostname": "Dell OTRO",
                "owner": "Javi Gutierrez",
                "avatar_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/hpspectre.jpg?alt=media&token=2d09092c-7c2d-43ec-bd79-0596b1596b9f",
                "status": 0
            }
        ]
    )

@app.route('/users', methods = ['GET'])
def getUsers():
    return jsonify([{
            "name": "Santi Hernandez",
            "email": "santi6minutos@iSecurity.com",
            "position": "Serucity Resarcher",
            "department": "Innovation",
            "device": "HP Pavilion",
            "image_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/santiago_foto.png?alt=media&token=3221114e-3fc2-4109-bd1a-42cd489029ef",
            "status": 1,
            "is_deleted": False
        },
        {
            "name": "Lucas Fernandez",
            "email": "lucasfer@iSecurity.com",
            "position": "Developer",
            "department": "Development",
            "device": "Macbook Pro 15",
            "image_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/Avatar%20Background.png?alt=media&token=316d1cf5-2f34-4ec5-87d8-304e686bdf36",
            "status": 1,
            "is_deleted": False,
            "events": []
        },
        {
            "name": "Javi Gutierrez",
            "email": "javiguz@iSecurity.com",
            "position": "Sys Admin",
            "department": "Development",
            "image_url": "https://firebasestorage.googleapis.com/v0/b/isecurity-176d0.appspot.com/o/javi.png?alt=media&token=b51e634e-c08a-417d-b1de-0f586960b21c",
            "status": 1,
            "is_deleted": False
        }
    ])

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

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True)