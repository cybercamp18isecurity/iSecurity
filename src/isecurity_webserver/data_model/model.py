from elasticsearch_sdk import ElasticSearcher
from .alerts import Alerts
from .users import Users
from .devices import Devices
from .domains import Domains

class Model(object):
    DEFAULT_INDEX = "isecurity_datamodel-*"
    def __init__(self, host, port=9200):
        self._elk = ElasticSearcher(host, port, self.DEFAULT_INDEX)
        self.alerts = Alerts(self._elk)
        self.domains = Domains(self._elk)
        self.devices = Devices(self._elk)
        self.users = Users(self._elk)

    def transform_query_to_response(self, data):
        response = []
        for element in data:
            data_elem = element['_source']
            data_elem["timestamp"] = data_elem.get('@datetime')
            data_elem["_id"] = element['_id']
            response.append(data_elem)
        return response