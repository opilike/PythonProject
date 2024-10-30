"""
File: Bouncing_ball.py
Name: Jason
-------------------------
ToDO: make a bouncing ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 100
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
#  make Bouncing check ball is bouncing or not
# bouncing = False
#  make Mouse_Click check mouse click or not
mouse_click = False
count_number = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball, mouse_click, count_number

    # first of ball
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)
    vy = 0
    while True:
        if mouse_click and count_number < 3:
            while True:
                ball.move(VX, vy)
                print(vy)
                #  if bounce to the bottom of window then VY = -VY
                if ball.y + ball.height > window.height and vy > 0:
                    vy = vy * REDUCE
                    vy = -vy
                else:
                    vy += GRAVITY
                pause(DELAY)
                #  if bounce out of window width
                if ball.x + ball.width > window.width:
                    break
            # init ball
            ball.x = START_X
            ball.y = START_Y
            # count how many times out of window
            count_number += 1
            # if out of window then make Mouse_Click false ,listen for mouse click again
            mouse_click = False
        pause(DELAY)


def bounce(mouse):
    global mouse_click
    mouse_click = True


if __name__ == "__main__":
    main()
