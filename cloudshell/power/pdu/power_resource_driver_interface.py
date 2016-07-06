from abc import ABCMeta
from abc import abstractmethod


class PowerResourceDriverInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_inventory(self, context):
        pass

    @abstractmethod
    def PowerOn(self, context, ports):
        pass

    @abstractmethod
    def PowerOff(self, context, ports):
        pass

    @abstractmethod
    def PowerCycle(self, context, ports, delay):
        pass