import time
from mapsparser.googlemapsparser import GoogleMapsParser
from mapsparser.constants import Const
# from searcher.brutforce import BrutForceSearch
from searcher.antcolony import AntColonySearch


class Main:
    def __init__(self, points_: list) -> None:
        self._points_list = points_
        self._parser = GoogleMapsParser()
        times = self._prepare_travel_times()

        # times = [[500, 39, 141, 141, 42, 41, 101, 39, 44, 131],
        #          [36, 500, 11, 18, 17, 13, 20, 13, 22, 19],
        #          [43, 15, 500, 15, 14, 24, 27, 11, 13, 19],
        #          [45, 18, 17, 500, 1, 14, 31, 12, 6, 9],
        #          [45, 20, 19, 1, 500, 15, 33, 13, 7, 9],
        #          [39, 17, 25, 16, 17, 500, 30, 24, 18, 10],
        #          [1, 19, 24, 30, 29, 26, 500, 26, 35, 32],
        #          [41, 15, 14, 11, 10, 22, 28, 500, 9, 15],
        #          [44, 23, 16, 5, 6, 15, 36, 9, 500, 16],
        #          [31, 21, 18, 9, 10, 10, 38, 19, 18, 500]]

        # times = [[500, 32, 31, 45, 121, 135, 128, 130, 31, 32, 30, 38, 23, 23, 131],
        #          [33, 500, 20, 9, 21, 10, 30, 6, 6, 1, 11, 10, 24, 24, 12],
        #          [29, 20, 500, 20, 13, 14, 24, 13, 16, 20, 16, 11, 20, 15, 10],
        #          [40, 9, 20, 500, 23, 9, 35, 9, 13, 9, 13, 12, 30, 25, 15],
        #          [22, 21, 13, 26, 500, 16, 10, 20, 20, 21, 18, 18, 6, 6, 20],
        #          [32, 10, 16, 10, 15, 500, 24, 9, 10, 10, 11, 4, 20, 17, 14],
        #          [29, 28, 23, 35, 7, 25, 500, 26, 27, 28, 24, 28, 6, 9, 26],
        #          [32, 7, 18, 9, 20, 9, 29, 500, 5, 7, 8, 9, 22, 22, 11],
        #          [32, 5, 19, 13, 20, 8, 29, 5, 500, 5, 10, 9, 22, 22, 13],
        #          [33, 1, 20, 9, 21, 10, 30, 6, 6, 500, 11, 10, 24, 24, 12],
        #          [30, 10, 18, 15, 18, 11, 25, 8, 9, 10, 500, 15, 20, 20, 12],
        #          [35, 8, 13, 15, 18, 4, 31, 6, 7, 8, 14, 500, 27, 23, 15],
        #          [23, 22, 17, 31, 6, 21, 3, 20, 21, 22, 18, 25, 500, 7, 20],
        #          [30, 14, 6, 19, 13, 9, 17, 13, 13, 14, 11, 13, 13, 500, 12],
        #          [30, 14, 10, 19, 17, 13, 25, 12, 13, 14, 11, 9, 21, 19, 500]]
        # BrutForceSearch(times, self._points_list)
        AntColonySearch(times, self._points_list)

    def _prepare_travel_times(self) -> list:
        self._parser.prepare_maps_page()
        home_point = self._points_list[0][0]
        times_table = []
        for start, _ in self._points_list:
            times_list = []
            for finish, shop_working_8am in self._points_list:
                trip_time = Const.DEFAULT_TRIP_TIME
                if start != finish:
                    trip_time = self._parser.find_travel_time(start, finish)
                    time.sleep(Const.DELAY_BETWEEN_PARSING_QUERIES)
                    # we start travel from home, destination shop must work from 8AM
                    if start == home_point and not shop_working_8am:
                        trip_time += Const.PENALTY_8_AM
                times_list.append(trip_time)
            print(times_list)
            times_table.append(times_list)
        self._parser.quit()
        return times_table


if __name__ == '__main__':
    # list of tuple (address: str, shop_working_from_8AM: bool = True)
    # points = [
    #     ("ауэзова 8 минск", True),
    #     ("солтыса 189 минск", True),
    #     ("филимонова 13 1 минск", False),
    #     ("долгобродская 11 минск", False),
    #     ("долгобродская 10 1 минск", True),
    #     ("щербакова 29 минск", True),
    #     ("связистов 13 минск", False),
    #     ("багратиона 18а минск", True),
    #     ("уральская 12 минск", True),
    #     ("буденного 16а минск", False)]
    points = [
        ("ауэзова 8 минск", True),
        ("нестерова 94 минск", True),
        ("алтайская 66а минск", True),
        ("илимская 27 минск", True),
        ("партизанский 106 минск", False),
        ("охотская 135 1 минск", False),
        ("жилуновича 41 минск", False),
        ("нестерова 49 минск", False),
        ("нестерова 58 минск", True),
        # ("нестерова 94 минск", True),
        ("ангарская 62а минск", True),
        ("нестерова 2 минск", True),
        ("жилуновича 8 минск", True),
        ("партизанский 120 минск", True),
        ("ангарская 38 2 минск", False)]

    main = Main(points)
