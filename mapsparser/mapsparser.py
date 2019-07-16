"""Interface for different maps parsers"""
from abc import ABCMeta
from abc import abstractmethod


class MapsParser(metaclass=ABCMeta):
    @abstractmethod
    def prepare_maps_page(self) -> None:
        pass

    @abstractmethod
    def find_travel_time(self, starting_address: str,
                         destination_address: str) -> int:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass
