import pytest
from isecurity_webserver.users import Users

def test_get_all_users():
    user_manager = Users()
    list_data = user_manager.get_list_users()
    assert len(list_data) > 0
    assert type(list_data[0]["_source"]) == dict

def test_get_details_devices():
    user_manager = Users()
    user_data = user_manager.get_user_details("3")
    raise Exception(user_data)
    assert type(user_data) == dict
    assert user_data["name"] == "Lucas Fernandez"
    assert 'alerts' in user_data
    assert 'devices' in user_data
