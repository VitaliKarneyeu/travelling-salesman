import logging
import random
from typing import Tuple, List, Union, Dict

from mapsparser.constants import Const
from .search import Search


class AntColonySearch(Search):
    def __init__(self, times_table: List[List[int]], points: List[Dict[str, Union[str, bool]]]) -> None:
        self._pheromone_table: List = []
        super().__init__(times_table, points)

    @staticmethod
    def _serch_max_benefit_index(times: list, pheromones: list, row_index: int) -> int:
        max_benefit = 0
        max_index = 0
        for column_index in range(len(times)):
            time = times[row_index][column_index]
            pheromone = pheromones[row_index][column_index]
            benefit = ((1 / time) ** Const.GREEDINESS) * (pheromone ** Const.HERD_INSTINCT)
            if benefit > max_benefit:
                max_benefit = benefit
                max_index = column_index
        return max_index

    def _prepare_pheromone_table(self, size: int) -> None:
        for _ in range(size):
            self._pheromone_table.append([Const.INITIAL_PHEROMONE_VALUE * random.random()] * size)

    def _calc_routes_data(self) -> None:
        size = len(self._time_table)
        self._pheromone_table = []
        self._prepare_pheromone_table(size)

        greediness = Const.GREEDINESS
        herd_instinct = Const.HERD_INSTINCT
        decay = Const.PHEROMONE_DECAY

        for _ in range(Const.NUMBER_ITERATIONS):
            sum_ant_reasons_to_travel = 0
            for row_index in range(size):
                for column_index in range(size):
                    travel_time = self._time_table[row_index][column_index]
                    pheromone_concentration = self._pheromone_table[row_index][column_index]
                    way_convenience = 1 / travel_time
                    sum_ant_reasons_to_travel += ((way_convenience ** greediness) *
                                                  (pheromone_concentration ** herd_instinct))

            for row_index in range(size):
                for column_index in range(size):

                    travel_time = self._time_table[row_index][column_index]
                    pheromone_concentration = self._pheromone_table[row_index][column_index]

                    way_convenience = 1 / travel_time
                    ant_travel_chance = ((way_convenience ** greediness) *
                                         (pheromone_concentration ** herd_instinct)
                                         / sum_ant_reasons_to_travel)

                    pheromone_amount_dropped_for_the_travel = 0
                    if random.random() * Const.RANDOM_SCOPE_COEFFICIENT < ant_travel_chance:
                        # if ant goes to travelling, he drops pheromone
                        pheromone_amount_dropped_for_the_travel = 1 / travel_time

                    new_pheromone_concentration = ((1 - decay) * pheromone_concentration +
                                                   pheromone_amount_dropped_for_the_travel)

                    self._pheromone_table[row_index][column_index] = new_pheromone_concentration

    def _build_route(self) -> Tuple[int, List[Tuple[str, str]]]:
        size = len(self._time_table)

        # create route
        travel_time = 0
        points_can_use = list(range(size))
        best_route = [(self._points[0][Const.ADDRESS_KEY], self._points[0][Const.DESCRIPTION_KEY])]
        points_can_use.remove(0)
        next_point_index = self._serch_max_benefit_index(self._time_table, self._pheromone_table, 0)
        travel_time += self._time_table[0][next_point_index]
        best_route.append((self._points[next_point_index][Const.ADDRESS_KEY],
                          self._points[next_point_index][Const.DESCRIPTION_KEY]))
        points_can_use.remove(next_point_index)
        for _ in range(size - 2):

            while True:
                max_benefit_index = self._serch_max_benefit_index(self._time_table, self._pheromone_table,
                                                                  next_point_index)
                if max_benefit_index in points_can_use:
                    travel_time += self._time_table[next_point_index][max_benefit_index]
                    next_point_index = max_benefit_index
                    break
                else:
                    # we traveled this way already
                    self._pheromone_table[next_point_index][max_benefit_index] = 0

            best_route.append((self._points[next_point_index][Const.ADDRESS_KEY],
                               self._points[next_point_index][Const.DESCRIPTION_KEY]))

            points_can_use.remove(next_point_index)

        # add way from last point to home
        best_route.append((self._points[0][Const.ADDRESS_KEY], self._points[0][Const.DESCRIPTION_KEY]))
        travel_time += self._time_table[next_point_index][0]
        return travel_time, best_route

    def search_fastest_way(self) -> None:
        time: int = 0
        best_route: List[Tuple[str, str]] = []

        need_calc = True
        while need_calc:
            need_calc = False
            self._calc_routes_data()
            time, best_route = self._build_route()

            # the second shop must start from 8am
            # for shop, start_8am in self._points:
            #     if best_route[Const.TO_SECOND] == shop and not start_8am:
            #         need_calc = True
            #         index_to = self._points.index((shop, start_8am))
            #         for shop_, flag_ in self._points:
            #             if best_route[Const.FROM_FIRST] == shop_:
            #                 index_from = self._points.index((shop_, flag_))
            #                 self._time_table[index_from][index_to] += Const.PENALTY_8_AM

        logging.info("Best route:")
        logging.info(f"total_time={time} min")
        for point in best_route:
            logging.info(point)
