import logging
import time
import json
from typing import List, Dict, Union

from mapsparser.googlemapsparser import GoogleMapsParser
from mapsparser.constants import Const
from searcher.antcolony import AntColonySearch


class Main:
    def __init__(self, points_: List[Dict[str, Union[str, bool]]]) -> None:
        self._points_list: List[Dict[str, Union[str, bool]]] = points_
        self._parser = GoogleMapsParser()
        times: List[List[int]] = self._prepare_travel_times()

        AntColonySearch(times, self._points_list)

    def _prepare_travel_times(self) -> List[List[int]]:
        self._parser.prepare_maps_page()
        home_point = self._points_list[0][Const.ADDRESS_KEY]
        times_table: List[List[int]] = []
        for start_point in self._points_list:
            start = start_point[Const.ADDRESS_KEY]
            times_list: List[int] = []
            for point in self._points_list:
                finish = point[Const.ADDRESS_KEY]
                shop_working_8am = point[Const.WORKS_AT_8AM_KEY]
                trip_time = Const.DEFAULT_TRIP_TIME
                if start != finish:
                    trip_time = self._parser.find_travel_time(start, finish)
                    time.sleep(Const.DELAY_BETWEEN_PARSING_QUERIES)
                    # we start travel from home, destination shop must work from 8AM
                    if start == home_point and not shop_working_8am:
                        trip_time += Const.PENALTY_8_AM
                times_list.append(trip_time)
            logging.info(times_list)
            times_table.append(times_list)
        self._parser.quit()
        return times_table


if __name__ == '__main__':
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        handlers=[stream_handler], level=logging.INFO)

    with open(Const.MAP_POINTS_FILENAME) as file:
        points = json.load(file)

    main = Main(points)
