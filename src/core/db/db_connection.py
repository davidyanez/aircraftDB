from abc import ABC, abstractmethod


class DBConnection(ABC):

    def __init__(self, config):
        self.config = config
        self.client = None

    @abstractmethod
    def get_db(self, **kwargs):
        pass

    @abstractmethod
    def create_db(self, **kwargs):
        pass


