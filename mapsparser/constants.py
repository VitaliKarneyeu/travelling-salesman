from selenium.webdriver.common.keys import Keys


class Const:
    DELAY_BETWEEN_PARSING_QUERIES = 2
    DEFAULT_TIME_STRING_TO_SET = (f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
                                  f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
                                  f"{Keys.DELETE}{Keys.DELETE}10:30 AM\n")
    DEFAULT_TRIP_TIME = 2500
    EXECUTABLE_PATH = r'./mapsparser/drivers/geckodriver'
    FIREFOX_DEFAULT_WINDOW_SIZE = "--window-size=1024,768"
    MINUTES_ONLY_PARTS_NUM = 2
    MINUTES_PER_HOUR = 60
    NEW_LINE_SYMBOL = "\n"
    PENALTY_8_AM = 1000     # for shops which not working early morning
    SPACE_SYMBOL = " "
    START_COUNT = 1
    STARTING_BEST_ROUTE_TIME = 888888888
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
