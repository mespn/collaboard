from dataclasses import dataclass

@dataclass(frozen=True)
class Colour:
    red: int
    green: int
    blue: int
    alpha: int = 255

# This is a list of standard colours.
BLACK = Colour(0,0,0)
WHITE = Colour(255,255,255)
RED = Colour(255,0,0)
GREEN = Colour(0,255,0)
BLUE = Colour(0,0,255)
YELLOW = Colour(255,255,0)
CYAN = Colour(0,255,255)
MAGENTA = Colour(255,0,255)
GRAY = Colour(128,128,128)
LIGHT_GRAY = Colour(192,192,192)
DARK_GRAY = Colour(64,64,64)
LIGHT_RED = Colour(255,128,128)