from data_model.model import Model
import pytest


def test_create_mode(elk_host):
    data = Model(elk_host, 9200)

def test_create_abstract_model_test(elk_host):
    data = Model(elk_host, 9200)


def test_create_model_alerts_not_found(elk_host):
    data = Model(elk_host, 9200)
    with pytest.raises(Exception):
        assert data.alerts.search("a", "b") == None
