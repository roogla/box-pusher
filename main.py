from math import floor
import blessed


def roundxy(x, y):
    return int(floor(x)), int(floor(y))

term = blessed.Terminal()
stauslen = None
status = None
x, y, xs, ys = 2, 3, 0.4, 0.4
with term.cbreak(), term.hidden_cursor():
    # clear the screen
    print(term.home + term.black_on_olivedrab4 + term.clear)
    val = ''
    # loop every 20ms
    while val.lower() != 'q':

        val = term.inkey(timeout=0.03)
        statuslen = len(str(val.name))
        if val.name == None:
            status = ""
        else:
            print(term.move_xy(*roundxy(0,0)) + term.black_on_olivedrab4("               "))
            status = term.home + term.black_on_olivedrab4(f"{val.name}: {statuslen}")
        # erase,
        txt_erase1 = term.move_xy(*roundxy(x, y)) + term.black_on_olivedrab4('    ')
        txt_erase2 = term.move_xy(*roundxy(x, y+1)) + term.black_on_olivedrab4('    ')
        txt_erase3 = term.move_xy(*roundxy(x, y+2)) + term.black_on_olivedrab4('    ')


        # bounce,
        if x >= (term.width - 3) or x <= 0 or val.name == "KEY_LEFT" or val.name == "KEY_RIGHT":
            xs *= -1
        if y >= term.height - 2 or y <= 2 or val.name == "KEY_UP" or val.name == "KEY_DOWN":
            ys *= -1

        # move,
        x, y = x + xs, y + ys

        # draw !
        txt_ball_1 = term.move_xy(*roundxy(x, y))
        txt_ball_2 = term.move_xy(*roundxy(x, y+1))
        txt_ball_3 = term.move_xy(*roundxy(x, y+2))
        print(txt_erase1 + txt_erase2 + txt_erase3
             +term.black_on_olivedrab4(f"{status}")
             +txt_ball_1 + term.on_blue('┌─┐')
             +txt_ball_2 + term.on_blue('└─┘'),
              end='', flush=True)
