from objects import Colour

'''
This is the base class for all drawable objects. It has a position and a color.
The position is stored as two floats: x and y, which are the coordinates of the top left corner of the
surrounding rectangle.
'''
class TwoDimensionDrawable:

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.colour = Colour.BLACK

    def set_colour(self, r:float, g:float, b:float):
        self.colour = Colour(r, g, b)   
        return self

    def set_colour(self, colour:Colour):
        self.colour = colour
        return self