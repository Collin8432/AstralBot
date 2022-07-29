code = '>vx>>x>>>vvx>x>x'        # commands:
color1, color2 = '#84f', '#218'  # > = go right
grid = 5, 5                      # v = go down
size = 25                        # x = switch color

from tkinter import Tk, Canvas
tk = Tk()
c = Canvas(tk, width = size * grid[0], height = size * grid[1], bg = color1)
c.pack()
x, y, state = 0, 0, [[0 for _ in range(grid[0])] for _ in range(grid[1])]
for i in code:
    if i == '>':
        if x == grid[0] - 1: x = 0
        else: x += 1
    if i == 'v':
        if y == grid[1] - 1: y = 0
        else: y += 1
    if i == 'x':
        if state[y][x]: c.create_rectangle(x * 25, y * 25, (x + 1) * 25, (y + 1) * 25, fill = color1, width = 0)
        else: c.create_rectangle(x * 25, y * 25, (x + 1) * 25, (y + 1) * 25, fill = color2, width = 0)
        state[y][x] = int(not bool(state[y][x]))