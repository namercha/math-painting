class Rectangle:
    """
    A rectangle shape that is drawn on the canvas object.
    """
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """
        Draws itself on the canvas.
        """
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    """
       A square shape that is drawn on the canvas object.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
        Draws itself on the canvas.
        """
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color