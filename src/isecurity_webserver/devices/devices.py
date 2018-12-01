from ..data_model import get_data_model

class Devices(object):
    def __init__(self):
        self.data_model = get_data_model()

    def get_list_devices(self, max_count=None):
        """
        Devuelve un listado de dispositivos, ordenados por estado y fecha.
        """
        query = {
            "sort": [
                { "status": { "order": "desc" }},
                { "@datetime": { "order": "desc" }}
            ],
            "size": 100
        }

        if max_count != None:
            max_count = int(max_count)
            query["size"] = max_count
            query['from'] = 0

        res = self.data_model.devices.query(query)
        return res

    def get_details_device(self, id_device):
        """
        Devuelve los detalles de un dispositivo, así como las alertas que le conciernen
        """
        device_data = self.data_model.devices.get(id_device)

        device = device_data['_source']
        device['id'] = device_data["_id"]

        device["alerts"] = self.data_model.alerts.search("id_external", id_device)
        device["related_alerts"] = self.get_related_events(device["alerts"], device["hostname"])

        user_id = device['owner']
        try:
            device['owner'] = self.data_model.users.get(user_id)
        except:
            pass

        return device

    def get_related_events(self, alerts, id_device):
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
