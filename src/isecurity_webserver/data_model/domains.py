from .abstract_model import AbstractModel

class Domains(AbstractModel):
    def __init__(self, elasticsearch):
        self.data_type = "domains"
        AbstractModel.__init__(self, elasticsearch, self.data_type)
