from typing import Tuple

from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, by: str, value: str) -> None:
        self._value: Tuple[str, str] = (by, value)

    def __call__(self, *args, **kwargs) -> Tuple[str, str]:
        return self._value[0], self._value[1].format(*args, **kwargs)


class MapsLocators:
    SEARCHBOX_DIRECTIONS_BUTTON = Locator(By.CSS_SELECTOR, '[aria-label="Directions"]')
    STARTING_ADDRESS_FIELD = Locator(By.CSS_SELECTOR, "#sb_ifc51 input")
    DESTINATION_ADDRESS_FIELD = Locator(By.CSS_SELECTOR, "#sb_ifc52 input")
    TRAVEL_MODE_TRANSIT_BUTTON = Locator(By.CSS_SELECTOR, '[aria-label="Transit"]')
    TRAVEL_MODE_WALKING_BUTTON = Locator(By.CSS_SELECTOR, '[aria-label="Walking"]')
    COULD_NOT_CALC = Locator(By.XPATH, "//div/jsl[contains(.,'could not calculate transit')]")
    TIME_INPUT = Locator(By.CSS_SELECTOR, '[name = "transit-time"]')
    SELECT_SCHEDULE_BUTTON = Locator(By.XPATH, "//div[@id=':4']")
    DEPART_MENU_ITEM = Locator(By.CSS_SELECTOR, "#\\:1 div")
    TRIP_DURATION_SECTION = Locator(By.XPATH, "//div[contains(@id, 'section-directions-trip-')]/div/div/div[1]/div[1]")
