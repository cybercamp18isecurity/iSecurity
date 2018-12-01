import pytest
from data_model.abstract_model import AbstractModel
from data_model.model import Model

class ModelTest(AbstractModel):
    def __init__(self, elasticsearch):
        self.data_type = "test"
        AbstractModel.__init__(self, elasticsearch, self.data_type)

@pytest.fixture()
def model_test(elk_host):
    model = Model(elk_host, 9200)
    test_model = ModelTest(model._elk)
    return test_model


def test_get(model_test):
    data = model_test.get(1)
    assert int(data['_id']) == 1

def test_search(model_test):
    data = model_test.search("id_external", "1234")
    assert int(data[0]['_id']) == 1

def test_query(model_test):
    query = {
        "query": {
            "term": {
                "id_external": "1234"
            }
        }
    }
    data = model_test.query(query)
    assert data[0]['_source']['id_external'] == "1234"

def test_create(model_test):
    data = {
        "id_external": "4321",
        "type": "0",
        "status": 0
    }
    id = "2"
    data = model_test.create(id, data)
    assert data == str(2)

def test_update(model_test):
    data = {
        "id_external": "2222",
        "type": "0",
        "status": 0
    }
    id = "3"
    data = model_test.create(id, data)
    assert data == id

    update_data = {
        "criticity": 1
    }
    data = model_test.update(id, update_data)
    assert data == id

    data_get = model_test.get(id)
    data = data_get["_source"]
    assert data['criticity'] == 1
    assert data['status'] == 0
    assert data['type'] == "0"
    assert data['id_external'] == "2222"
