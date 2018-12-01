import pytest
from isecurity_webserver.devices.devices import Devices

def test_get_all_devices():
    devices = Devices()
    devices_list = devices.get_list_devices()
    assert len(devices_list) > 0
    assert type(devices_list[0]["_source"]) == dict

def test_get_details_devices():
    devices = Devices()
    devices_data = devices.get_details_device("3")
    assert devices_data["hostname"] == "Macbook Pro 15"
