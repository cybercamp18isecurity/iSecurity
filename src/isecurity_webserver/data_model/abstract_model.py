class AbstractModel(object):
    INDEX_BASE = "isecurity_datamodel"

    def __init__(self, elasticsearch, data_type):
        self._elk = elasticsearch
        self.data_type = data_type
        self.index = "{}-{}".format(self.INDEX_BASE, self.data_type)

    def get(self, id):
        data = self._elk.get_from_elasticsearch(id, index=self.index)
        return data

    def search(self, key, value):
        """ Busca por una clave key-value exacta """

        query = {
            "query": {
                "term": {
                    str(key): str(value)
                }
            }
        }
        data = self._elk.make_query(query, index=self.index)
        return data['hits']

    def query(self, query):
        data = self._elk.make_query(query, index=self.index)
        return data['hits']

    def create(self, id, data):
        data = self._elk.create_document(id, data, index=self.index)
        return data

    def update(self, id, data):
        data = self._elk.update_document(id, data, index=self.index)
        return data
