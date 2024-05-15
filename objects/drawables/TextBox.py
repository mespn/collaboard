from TwoDimensionDrawable import TwoDimensionDrawable
from objects import Colour

class TextBox(TwoDimensionDrawable):
    SIZE = 12
    COLOUR = Colour.BLACK
    FONT = "Arial"

    def __init__(self, x, y, width, height, content=""):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.text = content
        self.colour = TextBox.COLOUR
        self.font = TextBox.FONT
        self.size = TextBox.SIZE
    
    def set_font(self, font:str):
        self.font = font
        return self

    def set_font_size(self, size:int):
        self.size = size
        return self
    