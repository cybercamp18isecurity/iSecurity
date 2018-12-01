from data_model.model import Model
from configparser import ConfigParser
import os

def get_data_model():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(dir_path, "configuration.ini")
    raise Exception(config_path)

    parser = ConfigParser()
    parser.read(config_path)

    host = parser.get('elasticsearch', 'host')
    port = parser.get('elasticsearch', 'port')
    data_model = Model(host, port)

    return data_model