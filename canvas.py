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
