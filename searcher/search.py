from abc import ABCMeta
from abc import abstractmethod


class Search(metaclass=ABCMeta):
    def __init__(self, times_table: list, points: list) -> None:
        self.search_fastest_way(times_table, points)

    @abstractmethod
    def search_fastest_way(self, times_table: list, points: list) -> None:
        pass
