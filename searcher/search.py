from abc import ABCMeta
from abc import abstractmethod


class Search(metaclass=ABCMeta):
    def __init__(self, times_table: list, points: list) -> None:
        self._time_table = times_table
        self._points = points
        self.search_fastest_way()

    @abstractmethod
    def search_fastest_way(self) -> None:
        pass
