import pytest
from isecurity_webserver.users import Users

def test_get_all_users():
    user_manager = Users()
    list_data = user_manager.get_list_users()
    assert len(list_data) > 0
    assert type(list_data[0]["_source"]) == dict

def test_get_all_users_limit():
    user_manager = Users()
    list_data = user_manager.get_list_users(max_count=1)
    assert len(list_data) == 1
    assert type(list_data[0]["_source"]) == dict


def test_get_details_devices():
    user_manager = Users()
    user_data = user_manager.get_user_details("3")
    assert type(user_data) == dict
    assert user_data["name"] == "Lucas Fernandez"
    assert 'alerts' in user_data
    assert 'devices' in user_data


def test_update_status_user():
    new_status = 1
    user_id = "3"
    user_manager = Users()
    user_data = user_manager.get_user_details(user_id)
    old_status = user_data['status']

    ok = user_manager.update_user_status(user_id, new_status)
    assert ok

    user_new_data = user_manager.get_user_details(user_id)
    assert str(user_new_data['status']) == str(new_status)

    ok = user_manager.update_user_status(user_id, old_status)
    assert ok
