import pytest
from isecurity_webserver.data_model import get_data_model

def test_load_data_model():
    data_model = get_data_model()
    assert len(data_model._elk._HOST) > 0