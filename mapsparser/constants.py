from selenium.webdriver.common.keys import Keys


class Const:
    FIREFOX_DEFAULT_WINDOW_SIZE = "--window-size=1024,768"
    EXECUTABLE_PATH = r'./mapsparser/drivers/geckodriver'
    GOOGLE_MAPS_URL = "https://www.google.com/maps/"
    GOOGLE_MAPS_PAGE_TITLE = "Google Maps"
    SEARCHBOX_DIRECTIONS_BUTTON_ID = ".searchbox-directions"
    STARTING_ADDRESS_FIELD_ID = "#sb_ifc51 input"
    DESTINATION_ADDRESS_FIELD_ID = "#sb_ifc52 input"
    TRAVEL_MODE_TRANSIT_BUTTON_ID = '[aria-label="Transit"]'
    SELECT_SCHEDULE_BUTTON_ID = "#\:4"
    DEPART_MENU_ITEM_ID = "#\:1 div"
    TIME_INPUT_ID = '[name = "transit-time"]'
    DEFAULT_TIME_STRING_TO_SET = (f"{Keys.BACKSPACE}{Keys.BACKSPACE}"
            f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
            f"{Keys.BACKSPACE}{Keys.BACKSPACE}10:30 AM\n")
    NEW_LINE_SYMBOL = "\n"
    TRIP_DURATION_SECTION_ID = ".section-directions-trip-duration"
    SPACE_SYMBOL = " "
    WEBDRIVER_TIMEOUT = 20
    DEFAULT_TRIP_TIME = 500
    PENALTY_8_AM = 100     # for shops not working early morning
    START_COUNT = 1
    STARTING_BEST_ROUTE_TIME = 888888888

    RANDOM_SCOPE_COEFFICIENT = 0.0001
    INITIAL_PHEROMONE_VALUE = 0.5
    PHEROMONE_DECAY = 0.05
    GREEDINESS = 0.2
    HERD_INSTINCT = 0.05
    DELAY_BETWEEN_PARSING_QUERIES = 2
