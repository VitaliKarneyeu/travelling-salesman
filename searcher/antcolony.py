import random
from mapsparser.constants import Const
from .search import Search


class AntColonySearch(Search):

    def search_fastest_way(self, time_table: list, points: list) -> None:
        size = len(time_table)
        pheromone_table = []
        for _ in range(size):
            pheromone_table.append([Const.INITIAL_PHEROMONE_VALUE] * size)

        greediness = Const.GREEDINESS
        herd_instinct = Const.HERD_INSTINCT
        decay = Const.PHEROMONE_DECAY

        for _ in range(1000):
            sum_ant_reasons_to_travel = 0
            for row_index in range(size):
                for column_index in range(size):
                    travel_time = time_table[row_index][column_index]
                    pheromone_concentration = pheromone_table[row_index][column_index]
                    way_convenience = 1 / travel_time
                    sum_ant_reasons_to_travel += ((way_convenience ** greediness) *
                                                  (pheromone_concentration ** herd_instinct))

            for row_index in range(size):
                for column_index in range(size):

                    travel_time = time_table[row_index][column_index]
                    pheromone_concentration = pheromone_table[row_index][column_index]

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

                    pheromone_table[row_index][column_index] = new_pheromone_concentration

        for row in pheromone_table:
            print(row)

        # create route
        travel_time = 0
        points_can_use = list(range(size))
        best_route = [points[0][0]]
        points_can_use.remove(0)
        next_point_index = pheromone_table[0].index(max(pheromone_table[0]))
        for _ in range(size - 1):

            while True:
                max_pheromone_value = max(pheromone_table[next_point_index])
                max_pheromone_index = pheromone_table[next_point_index].index(
                                                           max_pheromone_value)

                if max_pheromone_index in points_can_use:
                    travel_time += time_table[next_point_index][max_pheromone_index]
                    next_point_index = max_pheromone_index
                    break
                else:
                    # we traveled this way already
                    pheromone_table[next_point_index][max_pheromone_index] = 0

            best_route.append(points[next_point_index][0])
            points_can_use.remove(next_point_index)

        # add way from last point to home
        best_route.append(points[0][0])
        travel_time += time_table[next_point_index][0]

        print(travel_time, best_route)
