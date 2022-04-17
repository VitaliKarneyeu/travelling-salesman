from abc import ABCMeta
from abc import abstractmethod
from typing import List, Dict, Union


class Search(metaclass=ABCMeta):
    def __init__(self, times_table: List[List[int]], points: List[Dict[str, Union[str, bool]]]) -> None:
        self._time_table: List[List[int]] = times_table
        self._points: List[Dict[str, Union[str, bool]]] = points
        self.search_fastest_way()

    @abstractmethod
    def search_fastest_way(self) -> None:
        pass
