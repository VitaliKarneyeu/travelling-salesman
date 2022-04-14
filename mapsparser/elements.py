from typing import List, Tuple, Callable, Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from .constants import Const


class Element:
    _driver: WebDriver
    _default_condition: Callable = expected_conditions.presence_of_element_located

    def __init__(self, locator: Tuple[str, str], timeout: int = Const.WEBDRIVER_TIMEOUT) -> None:
        self._locator: Tuple[str, str] = locator
        self._timeout: int = timeout

    @property
    def driver(self) -> WebDriver:
        return Element._driver

    @staticmethod
    def set_driver(drv: WebDriver) -> None:
        Element._driver = drv

    @property
    def _element(self) -> Union[WebElement, List[WebElement]]:
        condition = self._default_condition(self._locator)
        return WebDriverWait(self.driver, self._timeout).until(condition)

    def _send_keys(self, value: str) -> None:
        self._element.send_keys(value)

    def _click(self) -> None:
        self._element.click()

    def _get_text(self) -> str:
        return self._element.text


class Field(Element):

    def send_keys(self, value: str) -> None:
        self._send_keys(value)

    def get_text(self) -> str:
        return self._get_text()

    def click(self):
        self._click()


class Fields(Element):

    @property
    def _element(self):
        condition = expected_conditions.presence_of_all_elements_located(self._locator)
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

        return WebDriverWait(self.driver, self._timeout, ignored_exceptions=ignored_exceptions).until(condition)

    def get_text_list(self) -> List[str]:
        return [element.text for element in self._element]


class Button(Field):
    def click(self):
        self._click()
