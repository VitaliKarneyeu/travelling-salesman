from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException

from .constants import Const
from .fields import Field, Fields, Button


class Page:
    def __init__(self, driver):
        self._driver = driver
        self._condition = None

    def sanity_check(self):
        return NotImplemented

    @property
    def driver(self) -> WebDriver:
        return self._driver


class MapsPage(Page):
    _URL = Const.GOOGLE_MAPS_URL
    _search_box_directions_button = Button(field_id=Const.SEARCHBOX_DIRECTIONS_BUTTON_ID,
                                           id_type=By.CSS_SELECTOR)  # type:Button
    _starting_address_field = Field(field_id=Const.STARTING_ADDRESS_FIELD_ID,
                                    id_type=By.CSS_SELECTOR)
    _destination_address_field = Field(field_id=Const.DESTINATION_ADDRESS_FIELD_ID,
                                       id_type=By.CSS_SELECTOR)
    _travel_mode_transit_button = Button(field_id=Const.TRAVEL_MODE_TRANSIT_BUTTON_ID,
                                         id_type=By.CSS_SELECTOR)
    _time_input_picker = Field(field_id=Const.TIME_INPUT_ID,
                               id_type=By.CSS_SELECTOR)
    _select_schedule_button = Field(field_id=Const.SELECT_SCHEDULE_BUTTON_ID,
                                    id_type=By.CSS_SELECTOR)
    _depart_menu_item = Field(field_id=Const.DEPART_MENU_ITEM_ID,
                              id_type=By.CSS_SELECTOR)
    _trip_duration_all_sections = Fields(field_id=Const.TRIP_DURATION_SECTION_ID,
                                         id_type=By.CSS_SELECTOR)

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self._URL)
        self.sanity_check()

    def sanity_check(self):
        assert Const.GOOGLE_MAPS_PAGE_TITLE in self.driver.title
        super().sanity_check()

    def click_search_box_directions_button(self):
        self._search_box_directions_button.click()

    def insert_starting_address(self, starting_address: str):
        self._starting_address_field = starting_address

    def insert_destination_address(self, destination_address: str):
        self._destination_address_field = destination_address

    def click_travel_mode_transit_button(self):
        self._travel_mode_transit_button.click()

    def set_default_time_to_field(self):
        self._time_input_picker.click()
        self._time_input_picker = Const.NEW_LINE_SYMBOL
        self._time_input_picker = Const.DEFAULT_TIME_STRING_TO_SET

    def click_select_schedule_button(self):
        self._select_schedule_button.click()

    def click_depart_menu_item(self):
        self._depart_menu_item.click()

    def get_shortest_trip_time(self) -> int:
        # reading data to list again and again, while all data not will
        # be read successfully
        durations_list = []
        success = False
        while not success:
            try:
                self._trip_duration_all_sections = Fields(
                    field_id=Const.TRIP_DURATION_SECTION_ID,
                    id_type=By.CSS_SELECTOR
                )
                durations_list = [trip.text for trip in self._trip_duration_all_sections]
                success = True
            except StaleElementReferenceException:
                pass

        # extract times from string list,
        trip_times = [int(time.split(Const.SPACE_SYMBOL)[0]) for time in durations_list]
        shortest_trip_time = min(trip_times)
        return shortest_trip_time
