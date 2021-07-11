from math import floor
import blessed
import sys

"""
Box pushing with limited ai interaction.
"""

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=100))
term = blessed.Terminal()
key_status = None
stauslen = None
move = False
screen_draw = True
x, y, xs, ys = 15, 3, 0.4, 0.4
path_coords = [(15, 3),(15, 4),(15, 5),(15, 6),
               (15, 7),(15, 8),(15, 9),(15, 10),
               (15, 11),(15, 12),(15, 13),(15, 14),
               (15, 15),(15, 16),(15, 17),(15, 18),
               (15, 19),(15, 20),(15, 21),(15, 22),
               (15, 23),(15, 24),(15, 25),(15, 26),
               (15, 27),(15, 28),(15, 29),(15, 30)]

def roundxy(x: int, y: int) -> int:
    return int(floor(x)), int(floor(y))

with term.cbreak(), term.hidden_cursor(), term.fullscreen():
    # clear screen and set color
    print(term.home + term.black_on_black + term.clear)
    print(term.home + term.black_on_olivedrab4(f"{key_status}"))
    val = ''

    # check val for quit condition
    while val.lower() != 'q':
        # loop ever 30ms
        val = term.inkey(timeout=0.03)
        scope_issue_key = val.name
        statuslen = len(str(val.name))

        # outputs key pressed to terminal line 1
        if val.name == None:
            key_status = ""
        else:
            print(term.move_xy(*roundxy(0,0)) + term.black_on_olivedrab4("               "))
            key_status = term.home + term.black_on_olivedrab4(f"{val.name}: {statuslen}")

        # erase,
        txt_erase1 = term.move_xy(*roundxy(x, y)) + term.black_on_olivedrab4('   ')
        txt_erase2 = term.move_xy(*roundxy(x, y+1)) + term.black_on_olivedrab4('   ')


        # directional logic
        if val.name == "KEY_DOWN":
                move = True
        if move:
            if y >= path_coords[27][1]:
                pass
            else:
                y += 0.3

        txt_ball_1 = term.move_xy(*roundxy(x, y))
        txt_ball_2 = term.move_xy(*roundxy(x, y+1))

        if screen_draw:
            print(txt_erase1 + txt_erase2
                +term.black_on_olivedrab4(f"{key_status}")
                +term.move_xy(*roundxy(path_coords[0][0], path_coords[0][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[1][0], path_coords[1][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[2][0], path_coords[2][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[3][0], path_coords[3][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[4][0], path_coords[4][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[5][0], path_coords[5][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[6][0], path_coords[6][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[7][0], path_coords[7][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[8][0], path_coords[8][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[9][0], path_coords[9][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[10][0], path_coords[10][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[11][0], path_coords[11][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[12][0], path_coords[12][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[13][0], path_coords[13][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[14][0], path_coords[14][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[15][0], path_coords[15][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[16][0], path_coords[16][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[17][0], path_coords[17][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[18][0], path_coords[18][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[19][0], path_coords[19][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[20][0], path_coords[20][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[21][0], path_coords[21][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[22][0], path_coords[22][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[23][0], path_coords[23][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[24][0], path_coords[24][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[25][0], path_coords[25][1])) + term.black_on_olivedrab4('   ')
                +term.move_xy(*roundxy(path_coords[26][0], path_coords[26][1])) + term.on_teal('   ')
                +term.move_xy(*roundxy(path_coords[27][0], path_coords[27][1])) + term.on_teal('   ')
                +txt_ball_1 + term.on_orange('┌─┐')
                +txt_ball_2 + term.on_orange('└─┘'),
                end='', flush=True)
        else:
            pass

        a,b = path_coords[27]
        if (roundxy(x, y + 1)) == (roundxy(a, b)):
            x = 500
            print(term.home + term.clear + term.move_y(term.height // 2))
            print(term.black_on_darkkhaki(term.center('You Won!')))
            screen_draw = False
