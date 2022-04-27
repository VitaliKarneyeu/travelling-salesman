from selenium.webdriver.common.keys import Keys


class Const:
    ADDRESS_KEY: str = "address"
    DELAY_UI: int = 3
    DELAY_BETWEEN_PARSING_QUERIES: int = 2
    DEFAULT_TIME_STRING_TO_SET: str = (f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
                                       f"{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}{Keys.BACKSPACE}"
                                       f"{Keys.DELETE}{Keys.DELETE}10:30 AM\n")
    DEFAULT_TRIP_TIME: int = 2500
    DESCRIPTION_KEY: str = "description"
    WEBDRIVER_EXECUTABLE_DIR: str = r'./mapsparser/drivers'
    FIREFOX_DEFAULT_WINDOW_SIZE: str = "--window-size=1024,768"
    MINUTES_ONLY_PARTS_NUM: int = 2
    MINUTES_PER_HOUR: int = 60
    NEW_LINE_SYMBOL: str = "\n"
    PENALTY_8_AM: int = 1000     # for shops which not working early morning
    SPACE_SYMBOL: str = " "
    START_COUNT: int = 1
    STARTING_BEST_ROUTE_TIME: int = 888888888
    WEBDRIVER_TIMEOUT: int = 20
    WITH_HOURS_PARTS_NUM: int = 4
    WORKS_AT_8AM_KEY: str = "works_at_8am"
    MAP_POINTS_FILENAME: str = "map_points.json"

    # constants for ant colony algorithm
    RANDOM_SCOPE_COEFFICIENT: float = 0.001
    INITIAL_PHEROMONE_VALUE: int = 1
    PHEROMONE_DECAY: float = 0.05
    GREEDINESS: float = 0.05
    HERD_INSTINCT: float = 0.5
    NUMBER_ITERATIONS: int = 2000
    FROM_FIRST: int = 1
    TO_SECOND: int = 2

