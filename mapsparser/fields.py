from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Field:
    _default_condition = expected_conditions.presence_of_element_located

    def __init__(self, field_id, id_type):
        self._field_id = field_id
        self._id_type = id_type
        self._element = None

    def __get__(self, instance, owner):
        web_driver = instance.driver  # type: WebDriver
        condition = self._default_condition((self._id_type, self._field_id))
        self._element = WebDriverWait(web_driver, 10).until(condition)
        return self._element

    def __set__(self, instance, value):
        self.__get__(instance, None)    # I don't know which 'owner' to send :(
        self._element.send_keys(value)


class Fields(Field):
    _default_condition = expected_conditions.presence_of_all_elements_located


class Button(Field):
    def click(self):
        self.click()
