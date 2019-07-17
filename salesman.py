from mapsparser.googlemapsparser import GoogleMapsParser
from mapsparser.constants import Const
from searcher.brutforce import BrutForceSearch


class Main:
    def __init__(self, points_: list) -> None:
        self._parser = GoogleMapsParser()
        self._points_list = points_
        times = self._prepare_travel_times()
        BrutForceSearch(times, self._points_list)

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
    points = [
        ("ауэзова 8 минск", True),
        ("солтыса 189 минск", True),
        ("филимонова 13 1 минск", False),
        ("долгобродская 11 минск", False),
        ("долгобродская 10 1 минск", True),
        ("щербакова 29 минск", True),
        ("связистов 13 минск", False),
        ("багратиона 18а минск", True),
        ("уральская 12 минск", True),
        ("буденного 16а минск", False)]

    main = Main(points)
