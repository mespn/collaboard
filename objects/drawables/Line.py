import objects.Colour as Colour
import Point

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_start_point(self)->Point:
        return Point(self.x1, self.y1)
    
    def get_end_point(self)->Point:
        return Point(self.x2, self.y2)