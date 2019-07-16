from mapsparser.googlemapsparser import GoogleMapsParser
from mapsparser.constants import Const


class Main:
    def __init__(self, points_: list) -> None:
        self._parser = GoogleMapsParser()
        self._points_list = points_
        self._prepare_travel_times()

    def _prepare_travel_times(self) -> None:
        self._parser.prepare_maps_page()
        times_table = []
        for start in self._points_list:
            times_list = []
            for finish in self._points_list:
                trip_time = Const.DEFAULT_TRIP_TIME
                if start != finish:
                    trip_time = self._parser.find_travel_time(start, finish)
                times_list.append(trip_time)
            print(times_list)
            times_table.append(times_list)
        print("================================")
        for i in times_table:
            print(i)
        self._parser.quit()


if __name__ == '__main__':
    points = [
        "ауэзова 8 минск",
        "солтыса 189 минск",
        "филимонова 13 1 минск",
        "долгобродская 11 минск",
        "долгобродская 10 1 минск",
        "щербакова 29 минск",
        "связистов 13 минск",
        "багратиона 18а минск",
        "уральская 12 минск",
        "буденного 16а минск"]

    main = Main(points)
