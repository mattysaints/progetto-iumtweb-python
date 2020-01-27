# costanti
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

# costanti del gioco
grid_thickness = 10
size = screen_width, screen_height = 420 + grid_thickness * 4, 420 + grid_thickness * 4
grid_color = white
cells = [
    ((screen_width - 4 * grid_thickness) / 6 + grid_thickness, (screen_height - 4 * grid_thickness) / 6 + grid_thickness),
    (screen_width / 2, (screen_height - 4 * grid_thickness) / 6 + grid_thickness),
    (screen_width - screen_width / 6 - grid_thickness / 2, (screen_height - 4 * grid_thickness) / 6 + grid_thickness),
    ((screen_width - 4 * grid_thickness) / 6 + grid_thickness, screen_height / 2),
    (screen_width / 2, screen_height / 2),
    (screen_width - screen_width / 6 - grid_thickness / 2, screen_height / 2),
    ((screen_width - 4 * grid_thickness) / 6 + grid_thickness, (screen_height - 4 * grid_thickness) / 6 * 5 + 3 * grid_thickness),
    (screen_width / 2, (screen_height - 4 * grid_thickness) / 6 * 5 + 3 * grid_thickness),
    (screen_width - screen_width / 6 - grid_thickness / 2, (screen_height - 4 * grid_thickness) / 6 * 5 + 3 * grid_thickness)
]
left_border = (0, 0, grid_thickness, screen_height)
right_border = (screen_width - grid_thickness, 0, grid_thickness, screen_height)
top_border = (0, 0, screen_width, grid_thickness)
bottom_border = (0, screen_height - grid_thickness, screen_width, grid_thickness)
vert_line_1 = ((screen_width - 2 * grid_thickness) / 3 + grid_thickness / 2, 0, grid_thickness, screen_height)
vert_line_2 = ((screen_width - 2 * grid_thickness) / 3 * 2 + grid_thickness / 2, 0, grid_thickness, screen_height)
oriz_line_1 = (0, (screen_height - 2 * grid_thickness) / 3 + grid_thickness / 2, screen_width, grid_thickness)
oriz_line_2 = (0, (screen_height - 2 * grid_thickness) / 3 * 2 + grid_thickness / 2, screen_width, grid_thickness)
