# costanti
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

# costanti del gioco
gThickness = 10
size = width, height = 420 + gThickness * 4, 420 + gThickness * 4
grid_color = white
cells = [
    ((width - 4 * gThickness) / 6 + gThickness, (height - 4 * gThickness) / 6 + gThickness),
    (width / 2, (height - 4 * gThickness) / 6 + gThickness),
    (width - width / 6 - gThickness / 2, (height - 4 * gThickness) / 6 + gThickness),
    ((width - 4 * gThickness) / 6 + gThickness, height / 2),
    (width / 2, height / 2),
    (width - width / 6 - gThickness / 2, height / 2),
    ((width - 4 * gThickness) / 6 + gThickness, (height - 4 * gThickness) / 6 * 5 + 3 * gThickness),
    (width / 2, (height - 4 * gThickness) / 6 * 5 + 3 * gThickness),
    (width - width / 6 - gThickness / 2, (height - 4 * gThickness) / 6 * 5 + 3 * gThickness)
]
left_border = (0, 0, gThickness, height)
right_border = (width - gThickness, 0, gThickness, height)
top_border = (0, 0, width, gThickness)
bottom_border = (0, height - gThickness, width, gThickness)
vert_line_1 = ((width - 2 * gThickness) / 3 + gThickness / 2, 0, gThickness, height)
vert_line_2 = ((width - 2 * gThickness) / 3 * 2 + gThickness / 2, 0, gThickness, height)
oriz_line_1 = (0, (height - 2 * gThickness) / 3 + gThickness / 2, width, gThickness)
oriz_line_2 = (0, (height - 2 * gThickness) / 3 * 2 + gThickness / 2, width, gThickness)

cpu = False
