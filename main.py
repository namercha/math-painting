from canvas import Canvas
from shapes import Rectangle, Square

# Get the height and width of the canvas from the user
canvas_width = int(input("Enter the width of the canvas: "))
canvas_height = int(input("Enter the height of the canvas: "))

# Store dictionary of color codes for background
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}
canvas_color = input("Enter the color of the canvas (black or white): ")

# Create the canvas
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape = input("What would you like to draw (square or rectangle). Enter quit to quit. ")

    if shape.lower() == "quit":
        break

    shape_x = int(input(f"Enter the x coordinate of the {shape}: "))
    shape_y = int(input(f"Enter the y coordinate of the {shape}: "))
    red = int(input("How much red should the rectangle have (between 0 and 255): "))
    green = int(input("How much green should the rectangle have (between 0 and 255): "))
    blue = int(input("How much blue should the rectangle have (between 0 and 255): "))

    if shape.lower() == "rectangle":
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

        rectangle = Rectangle(x=shape_x, y=shape_y, height=height, width=width, color=(red, green, blue))
        rectangle.draw(canvas)

    if shape.lower() == "square":
        side = int(input("Enter a value for the side of hte square: "))

        square = Square(x=shape_x, y=shape_y, side=side, color=(red, green, blue))
        square.draw(canvas)

canvas.make("canvas.png")
