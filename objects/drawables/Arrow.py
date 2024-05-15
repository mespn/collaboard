import Line

class Arrow(Line):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.angle = 60 # Represents the angle of the arrow head in degrees
        filled = False # Represents whether the arrow head is filled or not