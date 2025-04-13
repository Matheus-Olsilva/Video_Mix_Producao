from manim import *

# Frame settings
FRAME_WIDTH = 12
FRAME_HEIGHT = 8
BACKGROUND_COLOR = "#000000"

# Colors
HIGHLIGHT_COLOR = "#605CEA"
ARROW_COLOR = "#4E4AE8"
SECONDARY_COLOR = "#77CF7B"

# File paths (modify these to your actual paths)
ASSETS_DIR = "./assets"
LOGO_PATH = f"{ASSETS_DIR}/harumi_logo.png"
FACTORY_SVG = f"{ASSETS_DIR}/factory.svg"
MONEY_SVG = f"{ASSETS_DIR}/money.svg"
CHEESE_SVG = f"{ASSETS_DIR}/cheese.svg"
YOGURT_SVG = f"{ASSETS_DIR}/iorgute.svg"

# Text settings
DEFAULT_FONT = "IBM Plex Sans"
TITLE_FONT_SIZE = 35
SUBTITLE_FONT_SIZE = 28
TEXT_FONT_SIZE = 24
SMALL_TEXT_FONT_SIZE = 20

# Animation timing factors
# Use this multiplier to easily adjust all animation durations
TIMING_FACTOR = 1.0

# Production constraints
MIN_YOGURT = 320  # kg
MIN_CHEESE = 450  # kg

# Vertex coordinates
VERTICES = [
    (320, 450),      # R5 and R6 intersection
    (1457.14, 450),  # R1 and R6 intersection
    (1250, 812.5),   # R1 and R2 intersection
    (320, 1277.5)    # R2 and R5 intersection
]

# Constraint lines data
CONSTRAINTS = [
    {
        "name": "R1",
        "equation": "0.70x_1 + 0.40x_2 = 1200",
        "inequality": "0.70x_1 + 0.40x_2 \\leq 1200",
        "color": RED,
        "x_intercept": 1714.29,
        "y_intercept": 3000
    },
    {
        "name": "R2",
        "equation": "0.16x_1 + 0.32x_2 = 460",
        "inequality": "0.16x_1 + 0.32x_2 \\leq 460",
        "color": GREEN,
        "x_intercept": 2875,
        "y_intercept": 1437.5
    },
    {
        "name": "R3",
        "equation": "0.25x_1 + 0.33x_2 = 650",
        "inequality": "0.25x_1 + 0.33x_2 \\leq 650",
        "color": BLUE,
        "x_intercept": 2600,
        "y_intercept": 1969.7
    },
    {
        "name": "R4",
        "equation": "0.05x_1 + 0.09x_2 = 170",
        "inequality": "0.05x_1 + 0.09x_2 \\leq 170",
        "color": YELLOW,
        "x_intercept": 3400,
        "y_intercept": 1888.9
    },
    {
        "name": "R5",
        "equation": "x_1 = 320",
        "inequality": "x_1 \\geq 320",
        "color": PURPLE,
        "x_intercept": 320,
        "y_intercept": None  # Vertical line
    },
    {
        "name": "R6",
        "equation": "x_2 = 450",
        "inequality": "x_2 \\geq 450",
        "color": ORANGE,
        "x_intercept": None,  # Horizontal line
        "y_intercept": 450
    }
]

# Optimization parameters
OBJECTIVE_FUNCTION = {
    "yogurt_coef": 0.8,    # Profit per kg of yogurt
    "cheese_coef": 1.15,   # Profit per kg of cheese
    "equation": "Z = 0{,}8x_1 + 1{,}15x_2"
}

# Arrow groups for feasible region visualization
ARROW_GROUPS = {
    "horizontal_top": [
        ([390, 3500], [550, 3500]),
        ([390, 3350], [550, 3350]),
        ([390, 3200], [550, 3200]),
        ([390, 3050], [550, 3050]),
        ([390, 2900], [550, 2900]),
        ([390, 2750], [550, 2750]),
        ([390, 2600], [550, 2600]),
        ([390, 2450], [550, 2450])
    ],
    "diagonal": [
        ([600, 2400], [500, 2200]),
        ([650, 2300], [550, 2100]),
        ([710, 2200], [610, 2000]),
        ([770, 2100], [670, 1900]),
        ([830, 2000], [730, 1800]),
        ([890, 1900], [790, 1700]),
        ([950, 1800], [850, 1600]),
        ([1010, 1700], [910, 1500])
    ],
    "diagonal_long": [
        ([1050, 1600.0], [960, 1380.0]),
        ([1140, 1555.0], [1050, 1335.0]),
        ([1230, 1510.0], [1140, 1290.0]),
        ([1320, 1465.0], [1230, 1245.0]),
        ([1410, 1420.0], [1320, 1200.0]),
        ([1500, 1375.0], [1410, 1155.0]),
        ([1590, 1330.0], [1500, 1110.0]),
        ([1680, 1285.0], [1590, 1065.0]),
        ([1770, 1240.0], [1680, 1020.0]),
        ([1860, 1195.0], [1770, 975.0]),
        ([1950, 1150.0], [1860, 930.0]),
        ([2040, 1105.0], [1950, 885.0]),
        ([2130, 1060.0], [2040, 840.0]),
        ([2220, 1015.0], [2130, 795.0]),
        ([2310, 970.0], [2220, 750.0]),
        ([2400, 925.0], [2310, 705.0]),
        ([2490, 880.0], [2400, 660.0]),
        ([2580, 835.0], [2490, 615.0]),
        ([2670, 790.0], [2580, 570.0])
    ],
    "vertical_right": [
        ([2710, 550], [2710, 800]),
        ([2800, 550], [2800, 800]),
        ([2900, 550], [2900, 800]),
        ([3000, 550], [3000, 800]),
        ([3100, 550], [3100, 800]),
        ([3200, 550], [3200, 800]),
        ([3300, 550], [3300, 800]),
        ([3400, 550], [3400, 800]),
        ([3500, 550], [3500, 800]),
        ([3600, 550], [3600, 800]),
        ([3700, 550], [3700, 800]),
        ([3800, 550], [3800, 800]),
        ([3900, 550], [3900, 800]),
    ]
}