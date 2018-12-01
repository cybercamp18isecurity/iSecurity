from ..data_model import get_data_model

class Alerts(object):
    def __init__(self):
        self.data_model = get_data_model()

    def get_list_alerts(self, max_count=None):
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

        res = self.data_model.alerts.query(query)
        transformed_res = self.data_model.transform_query_to_response(res)
        return transformed_res

    def get_alert_details(self, id_alert):
        """
        Devuelve los detalles de un usuario, así como:
            - Sus alertas relacionadas
            - Sus dispositivos relacionados
        """
        alert_res = self.data_model.alerts.get(id_alert)
        alert_data = alert_res['_source']
        alert_data['_id'] = alert_res['_id']

        try:
            alert_data["devices"] = self.data_model.devices.search("hostname", alert_data['id_external'])
        except:
            alert_data["devices"] = None

        try:
            alert_data["user"] = self.data_model.users.get(alert_data['id_user'])
        except:
            alert_data["user"] = None

        return alert_data



    def update_alert_status(self, id_alert, status):
        res = self.data_model.alerts.update(id_alert, {"status": int(status)})
        return str(res) == str(id_alert)