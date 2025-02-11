from enum import Enum

# Section of special desk accomodations


class DeskAccomodations(Enum):
    NONE = None
    SIT_STAND_DESK = "sit_stand_desk"
    ERGO_KEYBOARD = "ergo_keyboard"
    ERGO_MOUSE = "ergo_mouse"
    SUN_SHADES = "sun_shades"


class DeskState(Enum):
    AVAILABLE = "avilable"
    SELECTED = "selected"
    BOOKED = "booked"
