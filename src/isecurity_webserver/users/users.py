
class Users(object):

    def get_list_users(self):
        users = [{
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
        }]
        return users