import numpy as np
from PIL import Image

# Create a 3d array of zeroes, then replace the zeroes (black pixels) with yellow pixels.
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Adds a red patch that is horizontal
data[1:3] = [255, 0, 0]

# Adding more colors
data[0:3, 0:2] = [255, 200, 233]
data[3:4, 1:4] = [45, 3, 233]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
