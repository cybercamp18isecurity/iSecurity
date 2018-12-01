from .abstract_model import AbstractModel

class Alerts(AbstractModel):
    def __init__(self, elasticsearch):
        self.data_type = "alerts"
        AbstractModel.__init__(self, elasticsearch, self.data_type)
