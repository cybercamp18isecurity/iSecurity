from ..data_model import get_data_model

class Users(object):
    def __init__(self):
        self.data_model = get_data_model()

    def get_list_users(self, max_count=None):
        query = {
            "sort": [
                { "status": { "order": "desc" }},
                { "@datetime": { "order": "desc" }}
            ]
        }
        if max_count != None:
            max_count = int(max_count)
            query["size"] = max_count
            query['from'] = 0

        res = self.data_model.users.query(query)
        return res


    def get_user_details(self, id_user):
        """
        Devuelve los detalles de un usuario, así como:
            - Sus alertas relacionadas
            - Sus dispositivos relacionados
        """
        user_res = self.data_model.users.get(id_user)
        user_data = user_res['_source']
        user_data['_id'] = user_res['_id']

        try:
            user_data["devices"] = self.data_model.devices.search("hostname", user_data['device'])
        except:
            user_data["devices"] = None

        try:
            user_data["alerts"] = self.data_model.alerts.search("id_user", id_user)
            user_data["related_alerts"] = self.get_related_events(user_data["alerts"])
        except:
            user_data["alerts"] = None

        return user_data


    def get_related_events(self, alerts):
        alerts_active = []
        alerts_working = []
        alerts_finished = []

        for alert in alerts:
            if alert['status'] == 0:
                alerts_active.append(alert)
            elif alerts['working'] == 1:
                alerts_working.append(alert)
            elif alerts['finished'] == 1:
                alerts_finished.append(alert)
        return {
            "alerts_active":alerts_active,
            "alerts_working":alerts_working,
            "alerts_finished": alerts_finished
        }

    def update_user_status(self, id_user, status):
        res = self.data_model.users.update(id_user, {"status": int(status)})
        return str(res) == str(id_user)