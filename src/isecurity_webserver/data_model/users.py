from .abstract_model import AbstractModel

class Users(AbstractModel):
    def __init__(self, elasticsearch):
        self.data_type = "users"
        AbstractModel.__init__(self, elasticsearch, self.data_type)
