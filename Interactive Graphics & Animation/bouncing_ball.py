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
bouncing = False
#  make Mouse_Click check mouse click or not
mouse_click = False
count_number = 0
vy = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # first of ball
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(mouse):
    global vy, ball, bouncing, mouse_click, count_number
    if bouncing is False:
        mouse_click = True
        vy = 0
        while True:
            print(vy)
            #  if bounce out of window width
            if ball.x + ball.width > window.width:
                # remove before ball
                window.remove(ball)
                # init ball
                ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                ball.filled = True
                #  make Bouncing check ball is bouncing or not
                window.add(ball)
                # count how many times out of window
                count_number += 1
                # if out of window then make Mouse_Click false ,listen for mouse click again
                mouse_click = False
                # if out of window then make Bouncing false, then can click and bouncing again
                bouncing = False
            #  if Mouse click and count_number <3 then can bounce
            elif mouse_click and count_number < 3:
                bouncing = True
                #  if bounce to the bottom of window then VY = -VY
                if ball.y + ball.height + vy > window.height:
                    vy = vy * REDUCE
                    vy = -vy
                    ball.move(VX, vy)
                else:
                    vy += GRAVITY
                    ball.move(VX, vy)
            pause(DELAY)


if __name__ == "__main__":
    main()
