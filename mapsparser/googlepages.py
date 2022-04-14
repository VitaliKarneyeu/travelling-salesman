from typing import Optional, NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

from .constants import Const
from .elements import Field, Fields, Button
from .locators import MapsLocators


class Page:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def sanity_check(self) -> Optional[NoReturn]:
        return NotImplemented

    @property
    def driver(self) -> WebDriver:
        return self._driver


class MapsPage(Page):
    URL = "https://www.google.com/maps/"
    title = "Google Maps"
    sanity_element = Button(MapsLocators.SEARCHBOX_DIRECTIONS_BUTTON())

    _search_box_directions_button = Button(MapsLocators.SEARCHBOX_DIRECTIONS_BUTTON())
    _starting_address_field = Field(MapsLocators.STARTING_ADDRESS_FIELD())
    _destination_address_field = Field(MapsLocators.DESTINATION_ADDRESS_FIELD())
    _travel_mode_transit_button = Button(MapsLocators.TRAVEL_MODE_TRANSIT_BUTTON())
    _travel_mode_walking_button = Button(MapsLocators.TRAVEL_MODE_WALKING_BUTTON())
    _could_not_calc_message_field = Field(MapsLocators.COULD_NOT_CALC())
    _time_input_picker = Field(MapsLocators.TIME_INPUT())
    _select_schedule_button = Field(MapsLocators.SELECT_SCHEDULE_BUTTON())
    _depart_menu_item = Field(MapsLocators.DEPART_MENU_ITEM())

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        driver.get(self.URL)
        self.sanity_check()

    def sanity_check(self) -> Optional[NoReturn]:
        assert self.title in self.driver.title
        self.sanity_element.set_driver(self.driver)
        super().sanity_check()

    def click_search_box_directions_button(self) -> None:
        self._search_box_directions_button.click()

    def send_keys_starting_address(self, value: str) -> None:
        self._starting_address_field.send_keys(value)

    def send_keys_destination_address(self, value: str) -> None:
        self._destination_address_field.send_keys(value)

    def click_travel_mode_transit_button(self) -> None:
        self._travel_mode_transit_button.click()

    def click_travel_mode_walking_button(self) -> None:
        self._travel_mode_walking_button.click()

    def set_default_time_to_field(self) -> None:
        self._time_input_picker.click()
        self._time_input_picker.send_keys(Const.NEW_LINE_SYMBOL)
        self._time_input_picker.send_keys(Const.DEFAULT_TIME_STRING_TO_SET)

    def click_select_schedule_button(self) -> None:
        self._select_schedule_button.click()

    def click_depart_menu_item(self) -> None:
        self._depart_menu_item.click()

    def get_shortest_trip_time(self) -> int:
        # reading data to list again and again, while all data not will
        # be read successfully, because DOM can changed suddenly
        durations_list = []
        success = False
        while not success:
            try:
                trip_duration_all_sections = Fields(MapsLocators.TRIP_DURATION_SECTION())
                durations_list = trip_duration_all_sections.get_text_list()
                success = True
            except StaleElementReferenceException:
                pass

        # extract times from string list,
        trip_times = []
        for time_string in durations_list:
            splitted_time_list = time_string.split(Const.SPACE_SYMBOL)
            if len(splitted_time_list) == Const.MINUTES_ONLY_PARTS_NUM:
                minutes, _ = splitted_time_list
                trip_times.append(int(minutes))
            elif len(splitted_time_list) == Const.WITH_HOURS_PARTS_NUM:
                hours, _, minutes, _ = splitted_time_list
                trip_times.append(
                    int(hours) * Const.MINUTES_PER_HOUR + int(minutes))
            else:
                raise ValueError("Wrong trip time answer from google maps!")
        shortest_trip_time = min(trip_times)
        return shortest_trip_time

    def get_sorry_message(self) -> str:
        try:
            return self._could_not_calc_message_field.get_text()
        except TimeoutException:
            return ""
