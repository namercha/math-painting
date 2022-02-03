import numpy as np
from PIL import Image


class Canvas:
    """
    Object that creates the shapes.
    """
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create a 3d numpy array of zeroes
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the zeroes into the color value
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Converts the current array into an image file.
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


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


canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')
