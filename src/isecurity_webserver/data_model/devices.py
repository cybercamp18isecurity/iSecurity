from .abstract_model import AbstractModel

class Devices(AbstractModel):
    def __init__(self, elasticsearch):
        self.data_type = "devices"
        AbstractModel.__init__(self, elasticsearch, self.data_type)
