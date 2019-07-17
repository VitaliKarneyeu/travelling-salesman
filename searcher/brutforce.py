from mapsparser.constants import Const


class BrutForceSearch:

    def search_fastest_way(self, times_table: list, points: list):
        size = len(times_table)

        best_route_time = Const.STARTING_BEST_ROUTE_TIME
        best_route = []

        counters_list = [Const.START_COUNT] * size

        finish = False
        while not finish:

            points_can_use = list(range(size))
            for num_digit in counters_list:
                if num_digit not in points_can_use:
                    break
                else:
                    points_can_use.remove(num_digit)
            else:
                # all digits are different, calculate new route len
                route_len = times_table[0][counters_list[0]]
                for i in range(len(counters_list) - 2):
                    route_len += times_table[counters_list[i]][counters_list[i+1]]
                route_len += times_table[counters_list[i+1]][0]
                if route_len < best_route_time:
                    # memorize best route
                    best_route = [points[0][0]]
                    for i in range(len(counters_list) - 1):
                        best_route.append(points[counters_list[i]][0])
                    best_route.append(points[0][0])
                    best_route_time = route_len

                    # print best route variant
                    print(best_route_time, best_route)
                    print("routes", times_table[0][counters_list[0]], end=' ')
                    for i in range(len(counters_list) - 2):
                        print(times_table[counters_list[i]][counters_list[i + 1]], end=' ')
                    print(times_table[counters_list[i+1]][0])
            # try to increment digits in counter_list
            accum = 1
            for i in range(len(counters_list)-1, -1, -1):
                if counters_list[i] + accum < size:
                    counters_list[i] += accum
                    accum = 0
                    break
                else:
                    counters_list[i] = 0
            else:
                finish = True
