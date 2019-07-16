"""Google maps parser"""
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from .constants import Const
from .mapsparser import MapsParser
from .googlepages import MapsPage


class GoogleMapsParser(MapsParser):
    def __init__(self):
        options = FirefoxOptions()
        options.add_argument(Const.FIREFOX_DEFAULT_WINDOW_SIZE)
        self._driver = webdriver.Firefox(firefox_options=options,
                                         executable_path=Const.EXECUTABLE_PATH)
        self._maps_page = MapsPage(self._driver)

    def prepare_maps_page(self) -> None:
        # maximize directions panel
        self._maps_page.click_search_box_directions_button()

    def find_travel_time(self, starting_address: str,
                         destination_address: str) -> int:
        # insert starting and destination points
        starting_address_string = f"{starting_address}\n"
        self._maps_page.insert_starting_address(starting_address_string)
        destination_address_string = f"{destination_address}\n"
        self._maps_page.insert_destination_address(destination_address_string)

        # select travel mode by bus-trolleybus
        self._maps_page.click_travel_mode_transit_button()

        self._maps_page.click_select_schedule_button()
        self._maps_page.click_depart_menu_item()

        # select default time
        self._maps_page.set_default_time_to_field()

        return self._maps_page.get_shortest_trip_time()

    def quit(self) -> None:
        self._driver.close()
        self._driver.quit()
