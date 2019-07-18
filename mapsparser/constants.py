from selenium.webdriver.common.keys import Keys


class Const:
    DELAY_BETWEEN_PARSING_QUERIES = 2
    DEFAULT_TIME_STRING_TO_SET = (f"{Keys.BACKSPACE}{Keys.BACKSPACE}"
            f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
            f"{Keys.BACKSPACE}{Keys.BACKSPACE}10:30 AM\n")
    DEFAULT_TRIP_TIME = 2500
    DEPART_MENU_ITEM_ID = "#\:1 div"
    DESTINATION_ADDRESS_FIELD_ID = "#sb_ifc52 input"
    EXECUTABLE_PATH = r'./mapsparser/drivers/geckodriver'
    FIREFOX_DEFAULT_WINDOW_SIZE = "--window-size=1024,768"
    GOOGLE_MAPS_URL = "https://www.google.com/maps/"
    GOOGLE_MAPS_PAGE_TITLE = "Google Maps"
    MINUTES_ONLY_PARTS_NUM = 2
    MINUTES_PER_HOUR = 60
    NEW_LINE_SYMBOL = "\n"
    PENALTY_8_AM = 1000     # for shops which not working early morning
    SEARCHBOX_DIRECTIONS_BUTTON_ID = ".searchbox-directions"
    SELECT_SCHEDULE_BUTTON_ID = "#\:4"
    SPACE_SYMBOL = " "
    START_COUNT = 1
    STARTING_ADDRESS_FIELD_ID = "#sb_ifc51 input"
    STARTING_BEST_ROUTE_TIME = 888888888
    TIME_INPUT_ID = '[name = "transit-time"]'
    TRAVEL_MODE_TRANSIT_BUTTON_ID = '[aria-label="Transit"]'
    TRIP_DURATION_SECTION_ID = ".section-directions-trip-duration"
    WEBDRIVER_TIMEOUT = 20
    WITH_HOURS_PARTS_NUM = 4

    # constants for ant colony algorithm
    RANDOM_SCOPE_COEFFICIENT = 0.001
    INITIAL_PHEROMONE_VALUE = 1
    PHEROMONE_DECAY = 0.05
    GREEDINESS = 0.05
    HERD_INSTINCT = 0.5
    NUMBER_ITERATIONS = 2000
    FROM_FIRST = 1
    TO_SECOND = 2
